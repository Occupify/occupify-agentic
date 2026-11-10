"""Local Git operations for the Occupify Contribution Sync Engine.

Executes subprocess-based git commands securely without shell injection (shell=False),
managing repo cloning/fetching, branch isolation, patch calculation, author retention,
conflict detection, and branch publishing.
"""

from __future__ import annotations

import logging
import os
import re
import subprocess
from typing import Any

logger = logging.getLogger(__name__)


class GitError(Exception):
    """Raised when a git command fails."""

    def __init__(
        self, message: str, returncode: int | None = None, stderr: str | None = None
    ) -> None:
        super().__init__(message)
        self.returncode = returncode
        self.stderr = stderr


def _sanitize(text: str, token: str | None = None) -> str:
    """Mask sensitive tokens or basic-auth credentials from logs/error messages."""
    if not text:
        return ""
    sanitized = text
    if token and token in sanitized:
        sanitized = sanitized.replace(token, "***")
    sanitized = re.sub(r"https://([^:]+):([^@]+)@", r"https://\1:***@", sanitized)
    sanitized = re.sub(r"ghp_[A-Za-z0-9_]+", "***", sanitized)
    sanitized = re.sub(r"github_pat_[A-Za-z0-9_]+", "***", sanitized)
    return sanitized


def _format_authenticated_url(url: str, token: str | None) -> str:
    """Format repository URL with authentication credentials safely."""
    if not token or not url.startswith("https://"):
        return url
    clean_url = re.sub(r"^https://[^@]+@", "https://", url)
    return clean_url.replace("https://", f"https://x-access-token:{token}@")


def _run_git(
    cmd: list[str],
    cwd: str | None = None,
    input_data: bytes | None = None,
    env: dict[str, str] | None = None,
    token: str | None = None,
    check: bool = False,
) -> subprocess.CompletedProcess[str]:
    """Execute a git command using subprocess.run with shell=False.

    Args:
        cmd: List of command arguments.
        cwd: Directory where the command will be executed.
        input_data: Optional bytes to pass to stdin.
        env: Optional environment variables.
        token: Optional token to mask in case of error.
        check: Whether to raise GitError on non-zero exit.

    Returns:
        CompletedProcess object.

    Raises:
        GitError: If command returns non-zero code and check is True.
    """
    try:
        proc = subprocess.run(
            cmd,
            cwd=cwd,
            input=input_data,
            capture_output=True,
            text=input_data is None,
            shell=False,
            env=env,
        )
    except Exception as exc:
        masked_cmd = " ".join(_sanitize(arg, token) for arg in cmd)
        logger.error("Failed to execute git process: %s: %s", masked_cmd, exc)
        raise GitError(f"Subprocess invocation failed: {exc}") from exc

    if check and proc.returncode != 0:
        stderr_text = (
            proc.stderr
            if isinstance(proc.stderr, str)
            else proc.stderr.decode("utf-8", errors="replace")
        )
        sanitized_stderr = _sanitize(stderr_text, token)
        masked_cmd = " ".join(_sanitize(arg, token) for arg in cmd)
        raise GitError(
            f"Git command failed ({proc.returncode}): {masked_cmd}\n{sanitized_stderr}",
            returncode=proc.returncode,
            stderr=sanitized_stderr,
        )

    return proc  # type: ignore[return-value]


class GitOps:
    """Git operations utility providing safe local repository management."""

    @staticmethod
    def clone_or_fetch(
        repo_url: str,
        target_dir: str,
        branch: str = "main",
        token: str | None = None,
    ) -> None:
        """Clone repository or fetch updates if target directory already exists.

        Args:
            repo_url: Remote Git URL (HTTPS or local path).
            target_dir: Local destination path.
            branch: Target branch to check out (default 'main').
            token: Optional GitHub token for authentication.
        """
        auth_url = _format_authenticated_url(repo_url, token)
        git_dir = os.path.join(target_dir, ".git")

        if os.path.isdir(target_dir) and os.path.isdir(git_dir):
            logger.info(
                "Target directory %s is an existing git repo. Fetching updates...", target_dir
            )
            # Update remote URL if authentication token provided
            if token:
                _run_git(
                    ["git", "remote", "set-url", "origin", auth_url],
                    cwd=target_dir,
                    token=token,
                    check=True,
                )

            # Fetch target branch
            _run_git(["git", "fetch", "origin", branch], cwd=target_dir, token=token, check=True)

            # Checkout and reset to origin/<branch>
            _run_git(["git", "checkout", branch], cwd=target_dir, token=token, check=False)
            _run_git(
                ["git", "reset", "--hard", f"origin/{branch}"],
                cwd=target_dir,
                token=token,
                check=True,
            )
            _run_git(["git", "clean", "-fd"], cwd=target_dir, token=token, check=True)
        else:
            logger.info(
                "Cloning %s into %s (branch: %s)...", _sanitize(repo_url, token), target_dir, branch
            )
            os.makedirs(os.path.dirname(os.path.abspath(target_dir)), exist_ok=True)

            # Attempt clone with branch
            clone_res = _run_git(
                ["git", "clone", "--branch", branch, auth_url, target_dir],
                token=token,
                check=False,
            )
            if clone_res.returncode != 0:
                # If branch doesn't exist yet on remote, clone default and create branch
                _run_git(["git", "clone", auth_url, target_dir], token=token, check=True)
                _run_git(["git", "checkout", "-B", branch], cwd=target_dir, token=token, check=True)

    @staticmethod
    def get_head_sha(repo_dir: str, branch: str = "main") -> str:
        """Retrieve commit SHA of branch HEAD.

        Args:
            repo_dir: Path to repository working directory.
            branch: Branch or ref name (default 'main').

        Returns:
            40-character commit SHA string.
        """
        proc = _run_git(["git", "rev-parse", branch], cwd=repo_dir, check=True)
        return proc.stdout.strip()

    @staticmethod
    def is_ancestor(repo_dir: str, ancestor_sha: str, descendant_sha: str = "HEAD") -> bool:
        """Verify whether ancestor_sha is reachable from descendant_sha.

        Args:
            repo_dir: Path to repository working directory.
            ancestor_sha: SHA to verify as ancestor.
            descendant_sha: Descendant commit ref (default 'HEAD').

        Returns:
            True if ancestor_sha is an ancestor of descendant_sha, False otherwise.
        """
        proc = _run_git(
            ["git", "merge-base", "--is-ancestor", ancestor_sha, descendant_sha],
            cwd=repo_dir,
            check=False,
        )
        return proc.returncode == 0

    @staticmethod
    def calculate_patch(repo_dir: str, base_sha: str, head_sha: str) -> str:
        """Calculate unified diff/patch between base_sha and head_sha.

        Args:
            repo_dir: Path to repository working directory.
            base_sha: Base commit SHA.
            head_sha: Head commit SHA.

        Returns:
            Unified diff string suitable for git apply.
        """
        proc = _run_git(
            ["git", "diff", "--binary", f"{base_sha}..{head_sha}"],
            cwd=repo_dir,
            check=True,
        )
        return proc.stdout

    @staticmethod
    def create_branch(repo_dir: str, new_branch: str, start_point: str = "HEAD") -> None:
        """Create and switch to a new branch from start_point.

        Args:
            repo_dir: Path to repository working directory.
            new_branch: Name of branch to create.
            start_point: Starting commit or ref (default 'HEAD').
        """
        _run_git(["git", "checkout", "-B", new_branch, start_point], cwd=repo_dir, check=True)

    @staticmethod
    def apply_patch_or_commit(
        repo_dir: str,
        patch_text: str,
        author_name: str,
        author_email: str,
        author_date: str,
        commit_message: str,
        co_authors: list[tuple[str, str]] | None = None,
    ) -> tuple[bool, str | None]:
        """Apply patch to current working directory and commit with strict author attribution.

        Preserves author metadata via --author flag and GIT_AUTHOR_DATE environment variable.
        Appends Co-authored-by trailers if co_authors are provided.
        Checks for conflicts before applying; on conflict or error, cleanly resets working tree.

        Args:
            repo_dir: Repository path.
            patch_text: Unified diff patch text.
            author_name: Original commit author name.
            author_email: Original commit author email.
            author_date: Original commit author date (ISO 8601 or git date format).
            commit_message: Commit message title and body.
            co_authors: Optional list of (Name, Email) tuples.

        Returns:
            Tuple of (success: bool, error_message: str | None).
        """
        if not patch_text or not patch_text.strip():
            logger.info("Patch is empty. No changes to apply.")
            return True, None

        patch_bytes = patch_text.encode("utf-8")

        # 1. Dry run check for conflicts
        check_proc = _run_git(
            ["git", "apply", "--check", "-"], cwd=repo_dir, input_data=patch_bytes
        )
        if check_proc.returncode != 0:
            stderr_msg = (
                check_proc.stderr
                if isinstance(check_proc.stderr, str)
                else check_proc.stderr.decode("utf-8", errors="replace")
            )
            conflict_msg = stderr_msg.strip() or "Patch conflict detected during git apply --check"
            logger.warning("Git apply --check failed: %s", conflict_msg)
            # Clean working directory
            _run_git(["git", "reset", "--hard", "HEAD"], cwd=repo_dir, check=False)
            _run_git(["git", "clean", "-fd"], cwd=repo_dir, check=False)
            return False, conflict_msg

        # 2. Apply patch
        apply_proc = _run_git(
            ["git", "apply", "--whitespace=nowarn", "-"],
            cwd=repo_dir,
            input_data=patch_bytes,
        )
        if apply_proc.returncode != 0:
            stderr_msg = (
                apply_proc.stderr
                if isinstance(apply_proc.stderr, str)
                else apply_proc.stderr.decode("utf-8", errors="replace")
            )
            err_msg = f"Failed applying patch: {stderr_msg.strip()}"
            logger.error(err_msg)
            _run_git(["git", "reset", "--hard", "HEAD"], cwd=repo_dir, check=False)
            _run_git(["git", "clean", "-fd"], cwd=repo_dir, check=False)
            return False, err_msg

        # 3. Stage all modified and new files
        _run_git(["git", "add", "-A"], cwd=repo_dir, check=True)

        # 4. Check if there are staged changes to commit
        status_proc = _run_git(["git", "status", "--porcelain"], cwd=repo_dir, check=True)
        if not status_proc.stdout.strip():
            logger.info("No modifications staged after applying patch.")
            return True, None

        # 5. Format commit message with Co-authored-by trailers
        formatted_message = commit_message.strip()
        if co_authors:
            trailers = [
                f"Co-authored-by: {name.strip()} <{email.strip()}>"
                for name, email in co_authors
                if name.strip() and email.strip()
            ]
            if trailers:
                formatted_message = f"{formatted_message}\n\n" + "\n".join(trailers)

        # 6. Commit with author retention
        author_flag = f"{author_name.strip()} <{author_email.strip()}>"
        env = os.environ.copy()
        env["GIT_AUTHOR_NAME"] = author_name.strip()
        env["GIT_AUTHOR_EMAIL"] = author_email.strip()
        if author_date:
            env["GIT_AUTHOR_DATE"] = str(author_date).strip()

        # Committer info fallback
        if "GIT_COMMITTER_NAME" not in env:
            env["GIT_COMMITTER_NAME"] = "Occupify Sync Bot"
        if "GIT_COMMITTER_EMAIL" not in env:
            env["GIT_COMMITTER_EMAIL"] = "sync-bot@occupify.local"

        commit_proc = _run_git(
            ["git", "commit", f"--author={author_flag}", "-m", formatted_message],
            cwd=repo_dir,
            env=env,
            check=False,
        )

        if commit_proc.returncode != 0:
            stderr_msg = (
                commit_proc.stderr
                if isinstance(commit_proc.stderr, str)
                else commit_proc.stderr.decode("utf-8", errors="replace")
            )
            err_msg = f"Commit creation failed: {stderr_msg.strip()}"
            logger.error(err_msg)
            _run_git(["git", "reset", "--hard", "HEAD"], cwd=repo_dir, check=False)
            _run_git(["git", "clean", "-fd"], cwd=repo_dir, check=False)
            return False, err_msg

        return True, None

    @staticmethod
    def push_branch(
        repo_dir: str,
        branch_name: str,
        remote_url: str,
        token: str | None = None,
    ) -> None:
        """Push branch to remote repository securely.

        Args:
            repo_dir: Path to repository working directory.
            branch_name: Branch name to push.
            remote_url: Remote repository URL.
            token: Optional GitHub token.
        """
        auth_url = _format_authenticated_url(remote_url, token)
        logger.info("Pushing branch %s to remote %s...", branch_name, _sanitize(remote_url, token))
        _run_git(
            ["git", "push", "-u", auth_url, branch_name],
            cwd=repo_dir,
            token=token,
            check=True,
        )

    @staticmethod
    def is_clean_working_tree(repo_dir: str) -> bool:
        """Check whether repository working tree is clean.

        Args:
            repo_dir: Path to repository working directory.

        Returns:
            True if clean, False if dirty or error.
        """
        proc = _run_git(["git", "status", "--porcelain"], cwd=repo_dir, check=False)
        return proc.returncode == 0 and not proc.stdout.strip()

    @staticmethod
    def find_merged_prs_from_history(
        repo_dir: str,
        since_commit: str | None = None,
        branch: str = "main",
    ) -> list[dict[str, Any]]:
        """Extract merged pull requests directly from local git log history.

        Fallback mechanism when GitHub REST API is inaccessible without token.

        Args:
            repo_dir: Path to repository working directory.
            since_commit: Optional base commit SHA. Only PRs merged after this commit are returned.
            branch: Target branch name (default 'main').

        Returns:
            List of parsed PR dictionaries sorted chronologically by merge date.
        """
        import re

        range_arg = f"{since_commit}..HEAD" if since_commit else "HEAD"
        # Verify range_arg exists, otherwise fallback to HEAD
        if since_commit:
            check_proc = _run_git(
                ["git", "rev-parse", "--verify", since_commit], cwd=repo_dir, check=False
            )
            if check_proc.returncode != 0:
                range_arg = "HEAD"

        cmd = [
            "git",
            "log",
            "--merges",
            "--format=%H|%P|%cI|%s",
            range_arg,
        ]
        proc = _run_git(cmd, cwd=repo_dir, check=False)
        if proc.returncode != 0 or not proc.stdout.strip():
            return []

        pr_regex = re.compile(
            r"Merge pull request #(\d+) from (?:[a-zA-Z0-9_\-\.]+/)?([^\s\n]+)", re.IGNORECASE
        )
        branch_merge_regex = re.compile(
            r"Merge branch '([^']+)'(?: of [^\s]+)? into ([^\s\n]+)", re.IGNORECASE
        )

        results: list[dict[str, Any]] = []
        for line in proc.stdout.strip().split("\n"):
            parts = line.split("|", 3)
            if len(parts) < 4:
                continue
            commit_sha, parents_str, merged_at_str, subject = parts
            parents = parents_str.strip().split()
            if len(parents) < 2:
                continue

            pr_number: int | None = None
            source_branch: str | None = None

            pr_match = pr_regex.search(subject)
            if pr_match:
                pr_number = int(pr_match.group(1))
                source_branch = pr_match.group(2)
            else:
                branch_match = branch_merge_regex.search(subject)
                if branch_match:
                    source_branch = branch_match.group(1)
                    # Generate a pseudo PR number from last 6 digits of sha integer if missing
                    pr_number = int(commit_sha[:6], 16) % 100000

            if pr_number is not None and source_branch:
                results.append(
                    {
                        "number": pr_number,
                        "title": subject,
                        "merge_commit_sha": commit_sha,
                        "merged_at": merged_at_str,
                        "head_branch": source_branch,
                        "base_branch": branch,
                        "parent1_sha": parents[0],
                        "parent2_sha": parents[1],
                        "is_git_fallback": True,
                    }
                )

        # Sort chronologically by merge date (oldest to newest)
        results.sort(key=lambda x: str(x.get("merged_at", "")))
        return results

    @staticmethod
    def get_pr_commits_from_history(
        repo_dir: str,
        parent1_sha: str,
        parent2_sha: str,
    ) -> list[dict[str, Any]]:
        """Retrieve commits introduced by a merged PR using git log between parents.

        Args:
            repo_dir: Path to repository working directory.
            parent1_sha: First parent (target base commit).
            parent2_sha: Second parent (PR head commit).

        Returns:
            List of commit dictionaries formatted identically to GitHub API responses.
        """
        cmd = [
            "git",
            "log",
            "--format=%H|%an|%ae|%aI|%s",
            f"{parent1_sha}..{parent2_sha}",
        ]
        proc = _run_git(cmd, cwd=repo_dir, check=False)
        if proc.returncode != 0 or not proc.stdout.strip():
            return []

        commits: list[dict[str, Any]] = []
        for line in proc.stdout.strip().split("\n"):
            parts = line.split("|", 4)
            if len(parts) < 5:
                continue
            sha, name, email, date, msg = parts
            commits.append(
                {
                    "sha": sha,
                    "commit": {
                        "message": msg,
                        "author": {
                            "name": name,
                            "email": email,
                            "date": date,
                        },
                    },
                    "author": {
                        "login": email.split("@")[0] if "@" in email else name,
                        "id": None,
                    },
                }
            )
        return commits

    @staticmethod
    def get_pr_files_from_history(
        repo_dir: str,
        parent1_sha: str,
        parent2_sha: str,
    ) -> list[str]:
        """Retrieve list of modified files between parents using git diff.

        Args:
            repo_dir: Path to repository working directory.
            parent1_sha: First parent (target base commit).
            parent2_sha: Second parent (PR head commit).

        Returns:
            List of relative changed file paths.
        """
        cmd = ["git", "diff", "--name-only", f"{parent1_sha}..{parent2_sha}"]
        proc = _run_git(cmd, cwd=repo_dir, check=False)
        if proc.returncode != 0 or not proc.stdout.strip():
            return []
        return [f.strip() for f in proc.stdout.strip().split("\n") if f.strip()]

    @staticmethod
    def ensure_clean_working_tree(repo_dir: str) -> bool:
        """Ensure working directory is clean by resetting and removing untracked files if dirty.

        Args:
            repo_dir: Path to repository working directory.

        Returns:
            True if tree is clean (or cleaned successfully), False if unable to clean.
        """
        proc = _run_git(["git", "status", "--porcelain"], cwd=repo_dir, check=False)
        if proc.returncode != 0:
            return False

        if not proc.stdout.strip():
            return True

        logger.warning("Working tree at %s is dirty. Resetting and cleaning...", repo_dir)
        _run_git(["git", "reset", "--hard", "HEAD"], cwd=repo_dir, check=False)
        _run_git(["git", "clean", "-fd"], cwd=repo_dir, check=False)

        verify_proc = _run_git(["git", "status", "--porcelain"], cwd=repo_dir, check=False)
        return verify_proc.returncode == 0 and not verify_proc.stdout.strip()


# Module-level aliases for direct function imports
clone_or_fetch = GitOps.clone_or_fetch
get_head_sha = GitOps.get_head_sha
is_ancestor = GitOps.is_ancestor
calculate_patch = GitOps.calculate_patch
create_branch = GitOps.create_branch
apply_patch_or_commit = GitOps.apply_patch_or_commit
push_branch = GitOps.push_branch
ensure_clean_working_tree = GitOps.ensure_clean_working_tree
is_clean_working_tree = GitOps.is_clean_working_tree
