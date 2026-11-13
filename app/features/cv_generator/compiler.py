import asyncio
import os
import re
import shutil
import signal
import sys
import tempfile
import threading
from pathlib import Path
from typing import Protocol

import pypdfium2 as pdfium

from app.features.cv_generator.schemas import CvGenerationError

MAX_PDF_BYTES = 5 * 1024 * 1024
MAX_TEX_BYTES = 256 * 1024


class CvCompiler(Protocol):
    async def compile(self, tex: str) -> bytes: ...


def validate_pdf(body: bytes) -> int:
    if not body.startswith(b"%PDF-") or len(body) > MAX_PDF_BYTES:
        raise CvGenerationError("PDF_INVALID")
    try:
        with pdfium.PdfDocument(body) as doc:
            if pdfium.raw.FPDF_GetSecurityHandlerRevision(doc) >= 0:
                raise CvGenerationError("PDF_INVALID")
            pages = len(doc)
            if pages > 2:
                raise CvGenerationError(
                    "CONTENT_TOO_LONG", "CV vượt quá hai trang. Hãy rút gọn nội dung."
                )
            if pages < 1:
                raise CvGenerationError("PDF_INVALID")
            for index in range(pages):
                page = doc[index]
                try:
                    width, height = page.get_size()
                    if abs(width - 595.276) > 2 or abs(height - 841.89) > 2:
                        raise CvGenerationError("PDF_INVALID")
                finally:
                    page.close()
            return pages
    except CvGenerationError:
        raise
    except Exception:
        raise CvGenerationError("PDF_INVALID") from None


LATEXMK = "latexmk"
_COMPILE_SLOTS = threading.BoundedSemaphore(2)


async def _finish(task):
    """Finish cleanup even if the enclosing request is cancelled repeatedly."""
    while not task.done():
        try:
            await asyncio.shield(task)
        except asyncio.CancelledError:
            continue
    return task.result()


class LocalCvCompiler:
    """Run LaTeX inside the dedicated compiler container."""

    def __init__(self, *, timeout_s: float = 30):
        self.timeout_s = timeout_s

    async def compile(self, tex: str) -> bytes:
        body = tex.encode("utf-8")
        if len(body) > MAX_TEX_BYTES:
            raise CvGenerationError("INVALID_INPUT")
        binary = shutil.which(LATEXMK)
        if binary is None:
            raise CvGenerationError("COMPILER_UNAVAILABLE")
        if not _COMPILE_SLOTS.acquire(blocking=False):
            raise CvGenerationError("BUSY", retryable=True)
        try:
            with tempfile.TemporaryDirectory(prefix="cv-") as workdir:
                root = Path(workdir)
                (root / "cv.tex").write_bytes(body)
                env = {
                    "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
                    "HOME": workdir,
                    "TMPDIR": workdir,
                    "XDG_CACHE_HOME": workdir,
                    "LANG": "C.UTF-8",
                    "LC_ALL": "C.UTF-8",
                    "openin_any": "p",
                    "openout_any": "p",
                    "shell_escape": "0",
                    "TEXMFOUTPUT": workdir,
                }
                with (root / "process.log").open("wb") as output:
                    spawn = asyncio.create_task(
                        asyncio.create_subprocess_exec(
                            sys.executable,
                            "-I",
                            str(Path(__file__).with_name("latex_runner.py")),
                            binary,
                            "-norc",
                            "-xelatex",
                            "-no-shell-escape",
                            "-interaction=nonstopmode",
                            "-halt-on-error",
                            "cv.tex",
                            cwd=workdir,
                            env=env,
                            stdin=asyncio.subprocess.DEVNULL,
                            stdout=output,
                            stderr=asyncio.subprocess.STDOUT,
                            start_new_session=True,
                        )
                    )
                    process = None
                    try:
                        process = await asyncio.shield(spawn)
                        async with asyncio.timeout(self.timeout_s):
                            await process.wait()
                    except BaseException:
                        if process is None:
                            process = await _finish(spawn)
                        try:
                            os.killpg(process.pid, signal.SIGKILL)
                        except ProcessLookupError:
                            pass
                        await _finish(asyncio.create_task(process.wait()))
                        raise
                if process.returncode:
                    raise CvGenerationError("COMPILE_FAILED")
                log = root / "cv.log"
                if log.exists():
                    if log.stat().st_size > 2 * 1024 * 1024:
                        raise CvGenerationError("LAYOUT_INVALID")
                    if re.search(
                        r"Missing character:|Overfull \\[hv]box", log.read_text(errors="replace")
                    ):
                        raise CvGenerationError("LAYOUT_INVALID")
                pdf = root / "cv.pdf"
                if not pdf.is_file() or pdf.stat().st_size > MAX_PDF_BYTES:
                    raise CvGenerationError("COMPILE_FAILED")
                return pdf.read_bytes()
        except TimeoutError:
            raise CvGenerationError("COMPILE_TIMEOUT", retryable=True) from None
        except OSError:
            raise CvGenerationError("COMPILE_FAILED") from None
        finally:
            _COMPILE_SLOTS.release()
