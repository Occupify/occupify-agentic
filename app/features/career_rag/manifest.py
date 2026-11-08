import hashlib
from collections.abc import Sequence
from pathlib import Path


def compute_file_hash(file_path: str | Path) -> str:
    """Compute sha256 checksum for a single file."""
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def compute_directory_manifest_hash(dir_path: str | Path, pattern: str = "*.*") -> str:
    """Compute combined sha256 hash across sorted files in a directory."""
    path = Path(dir_path)
    if not path.exists():
        return hashlib.sha256(b"").hexdigest()

    files = sorted([f for f in path.rglob(pattern) if f.is_file()])
    manifest_hasher = hashlib.sha256()
    for f in files:
        rel_path = f.relative_to(path).as_posix()
        manifest_hasher.update(rel_path.encode("utf-8"))
        f_hash = compute_file_hash(f)
        manifest_hasher.update(f_hash.encode("utf-8"))
    return manifest_hasher.hexdigest()


def compute_files_manifest_hash(file_paths: Sequence[str | Path]) -> str:
    """Compute combined sha256 hash for a specific list of files."""
    manifest_hasher = hashlib.sha256()
    sorted_paths = sorted([Path(p) for p in file_paths if Path(p).is_file()])
    for f in sorted_paths:
        manifest_hasher.update(f.name.encode("utf-8"))
        f_hash = compute_file_hash(f)
        manifest_hasher.update(f_hash.encode("utf-8"))
    return manifest_hasher.hexdigest()


class ManifestRegistry:
    """Tracks ingestion runs and checks idempotency based on hashes."""

    def __init__(self) -> None:
        pass

    @staticmethod
    def is_hash_changed(current_hash: str, last_completed_hash: str | None) -> bool:
        if not last_completed_hash:
            return True
        return current_hash != last_completed_hash
