import tempfile
from pathlib import Path

from app.features.career_rag.manifest import (
    ManifestRegistry,
    compute_directory_manifest_hash,
    compute_file_hash,
    compute_files_manifest_hash,
)


def test_compute_file_hash():
    with tempfile.NamedTemporaryFile("w+", delete=False) as f:
        f.write("Career Ingestion Test Content")
        f_path = f.name

    try:
        h1 = compute_file_hash(f_path)
        h2 = compute_file_hash(f_path)
        assert len(h1) == 64
        assert h1 == h2

        # Change content
        with open(f_path, "a") as f:
            f.write(" appended")

        h3 = compute_file_hash(f_path)
        assert h3 != h1
    finally:
        Path(f_path).unlink(missing_ok=True)


def test_directory_manifest_hash():
    with tempfile.TemporaryDirectory() as tmpdir:
        p = Path(tmpdir)
        (p / "a.csv").write_text("col1,col2\n1,2")
        (p / "b.md").write_text("# Test Title")

        hash_before = compute_directory_manifest_hash(tmpdir)
        assert len(hash_before) == 64

        # Same directory gives exact same hash
        assert compute_directory_manifest_hash(tmpdir) == hash_before

        # Adding a file changes hash
        (p / "c.txt").write_text("another file")
        hash_after = compute_directory_manifest_hash(tmpdir)
        assert hash_after != hash_before


def test_files_manifest_hash():
    with tempfile.TemporaryDirectory() as tmpdir:
        p = Path(tmpdir)
        f1 = p / "f1.txt"
        f2 = p / "f2.txt"
        f1.write_text("Hello")
        f2.write_text("World")

        h = compute_files_manifest_hash([f1, f2])
        assert len(h) == 64
        assert compute_files_manifest_hash([f2, f1]) == h  # Order-independent sorting


def test_manifest_registry_idempotency():
    reg = ManifestRegistry()
    assert reg.is_hash_changed("hash1", None) is True
    assert reg.is_hash_changed("hash1", "hash1") is False
    assert reg.is_hash_changed("hash2", "hash1") is True
