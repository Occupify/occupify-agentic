import asyncio
import threading
import time
from pathlib import Path

import pytest
import respx

from app.features.cv_generator import compiler
from app.features.cv_generator.compiler import LocalCvCompiler, validate_pdf
from app.features.cv_generator.remote_compiler import RemoteCvCompiler
from app.features.cv_generator.schemas import CvGenerationError
from tests.unit.cv_generator.helpers import make_pdf


@pytest.mark.parametrize("pages", [1, 2])
def test_accepts_readable_a4_pdf(pages):
    assert validate_pdf(make_pdf(pages)) == pages


@pytest.mark.parametrize(
    ("body", "code"),
    [
        (b"not pdf", "PDF_INVALID"),
        (make_pdf(3), "CONTENT_TOO_LONG"),
        (make_pdf(size="letter"), "PDF_INVALID"),
        (b"%PDF" + b"x" * 5_242_880, "PDF_INVALID"),
    ],
)
def test_rejects_invalid_pdf_before_upload(body, code):
    with pytest.raises(CvGenerationError) as exc:
        validate_pdf(body)
    assert exc.value.code == code


def fake_latexmk(tmp_path, monkeypatch, body):
    script = tmp_path / "latexmk"
    script.write_text("#!/usr/bin/env python3\n" + body)
    script.chmod(0o700)
    monkeypatch.setattr(compiler, "LATEXMK", str(script))


async def test_local_compiler_clears_credentials_enforces_limits_and_removes_workdir(
    tmp_path, monkeypatch
):
    marker = tmp_path / "workdir"
    pdf = make_pdf()
    monkeypatch.setenv("OCI_SECRET_TEST", "not-for-compiler")
    fake_latexmk(
        tmp_path,
        monkeypatch,
        "import os,resource,sys\nfrom pathlib import Path\n"
        "assert 'OCI_SECRET_TEST' not in os.environ\n"
        "assert '-no-shell-escape' in sys.argv\n"
        "assert resource.getrlimit(resource.RLIMIT_FSIZE)[0] == 8 * 1024 * 1024\n"
        f"Path({str(marker)!r}).write_text(str(Path.cwd()))\n"
        f"Path('cv.pdf').write_bytes({pdf!r})\n"
        "Path('cv.log').write_text('ok')\n",
    )
    assert await LocalCvCompiler().compile("synthetic tex") == pdf
    assert not Path(marker.read_text()).exists()


async def test_local_compiler_sanitizes_failures(tmp_path, monkeypatch):
    fake_latexmk(tmp_path, monkeypatch, "import sys\nprint('private CV and secret')\nsys.exit(1)\n")
    with pytest.raises(CvGenerationError) as exc:
        await LocalCvCompiler().compile("private input")
    assert exc.value.code == "COMPILE_FAILED"
    assert "private" not in str(exc.value)


async def test_local_compiler_reports_missing_executable(monkeypatch):
    monkeypatch.setattr(compiler, "LATEXMK", "/no/such/latexmk")
    with pytest.raises(CvGenerationError) as exc:
        await LocalCvCompiler().compile("synthetic")
    assert exc.value.code == "COMPILER_UNAVAILABLE"


async def test_timeout_kills_compile_and_cleans_tempdir(tmp_path, monkeypatch):
    marker = tmp_path / "workdir"
    fake_latexmk(
        tmp_path,
        monkeypatch,
        "import time\nfrom pathlib import Path\n"
        f"Path({str(marker)!r}).write_text(str(Path.cwd()))\ntime.sleep(10)\n",
    )
    started = time.monotonic()
    with pytest.raises(CvGenerationError) as exc:
        await LocalCvCompiler(timeout_s=0.2).compile("synthetic")
    assert exc.value.code == "COMPILE_TIMEOUT"
    assert time.monotonic() - started < 3
    assert not Path(marker.read_text()).exists()


async def test_cancellation_reaps_compile_before_removing_workdir(tmp_path, monkeypatch):
    marker = tmp_path / "workdir"
    fake_latexmk(
        tmp_path,
        monkeypatch,
        "import time\nfrom pathlib import Path\n"
        f"Path({str(marker)!r}).write_text(str(Path.cwd()))\ntime.sleep(10)\n",
    )
    task = asyncio.create_task(LocalCvCompiler().compile("synthetic"))
    async with asyncio.timeout(3):
        while not marker.exists():
            await asyncio.sleep(0.01)
    task.cancel()
    with pytest.raises(asyncio.CancelledError):
        await task
    assert not Path(marker.read_text()).exists()


async def test_local_compiler_rejects_layout_warning(tmp_path, monkeypatch):
    fake_latexmk(
        tmp_path,
        monkeypatch,
        "from pathlib import Path\n"
        f"Path('cv.pdf').write_bytes({make_pdf()!r})\n"
        "Path('cv.log').write_text('Overfull \\\\hbox (30pt too wide)')\n",
    )
    with pytest.raises(CvGenerationError) as exc:
        await LocalCvCompiler().compile("synthetic")
    assert exc.value.code == "LAYOUT_INVALID"


async def test_local_compiler_returns_busy_without_starting_another_process(tmp_path, monkeypatch):
    fake_latexmk(tmp_path, monkeypatch, "raise AssertionError('must not start')\n")
    slots = threading.BoundedSemaphore(1)
    slots.acquire()
    monkeypatch.setattr(compiler, "_COMPILE_SLOTS", slots)
    with pytest.raises(CvGenerationError) as exc:
        await LocalCvCompiler().compile("synthetic")
    assert exc.value.code == "BUSY" and exc.value.retryable


async def test_local_compiler_rejects_oversize_input_before_spawning():
    with pytest.raises(CvGenerationError) as exc:
        await LocalCvCompiler().compile("x" * (256 * 1024 + 1))
    assert exc.value.code == "INVALID_INPUT"


async def test_remote_compiler_returns_pdf_from_internal_service():
    pdf = make_pdf()
    with respx.mock(assert_all_called=True) as mock:
        route = mock.post("http://cv-compiler:8190/compile").respond(200, content=pdf)
        assert await RemoteCvCompiler("http://cv-compiler:8190").compile("synthetic") == pdf
        assert route.called


async def test_remote_compiler_preserves_safe_busy_error():
    with respx.mock(assert_all_called=True) as mock:
        mock.post("http://cv-compiler:8190/compile").respond(429, json={"code": "BUSY"})
        with pytest.raises(CvGenerationError) as exc:
            await RemoteCvCompiler("http://cv-compiler:8190").compile("synthetic")
    assert exc.value.code == "BUSY" and exc.value.retryable
