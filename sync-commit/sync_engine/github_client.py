"""GitHub API client for the Occupify Contribution Sync Engine.

Provides resilient, authenticated interaction with GitHub REST API v3,
including rate-limiting backoff, PR queries, commit extraction, and PR creation.
"""

from __future__ import annotations

import logging
import random
import time
from typing import Any

import httpx

logger = logging.getLogger(__name__)

RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}


class GitHubAPIError(Exception):
    """Base exception for GitHub API errors."""

    def __init__(
        self, message: str, status_code: int | None = None, response_body: str | None = None
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.response_body = response_body


class GitHubRateLimitError(GitHubAPIError):
    """Raised when GitHub API rate limit is exceeded and retries are exhausted."""


class GitHubResourceNotFoundError(GitHubAPIError):
    """Raised when requested GitHub resource is not found (404)."""


class GitHubClient:
    """Client for interacting with GitHub REST API with exponential backoff retries."""

    def __init__(
        self,
        token: str | None = None,
        base_url: str = "https://api.github.com",
        timeout: float = 30.0,
        max_retries: int = 5,
        backoff_factor: float = 1.0,
        client: httpx.Client | None = None,
    ) -> None:
        """Initialize the GitHub API client.

        Args:
            token: Optional GitHub Personal Access Token or App Token.
            base_url: Base URL of GitHub API (defaults to https://api.github.com).
            timeout: Request timeout in seconds.
            max_retries: Maximum number of retry attempts on retryable status codes.
            backoff_factor: Multiplier for exponential backoff delay.
            client: Optional pre-configured httpx.Client (e.g. for testing with respx).
        """
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.timeout = timeout
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

        headers: dict[str, str] = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self.token:
            clean_token = self.token.strip()
            if not clean_token.lower().startswith("bearer "):
                headers["Authorization"] = f"Bearer {clean_token}"
            else:
                headers["Authorization"] = clean_token

        if client is not None:
            self._client = client
            self._owns_client = False
        else:
            self._client = httpx.Client(
                base_url=self.base_url,
                headers=headers,
                timeout=self.timeout,
            )
            self._owns_client = True

    def __enter__(self) -> GitHubClient:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.close()

    def close(self) -> None:
        """Close the underlying HTTP client session."""
        if self._owns_client and hasattr(self, "_client"):
            self._client.close()

    def _request(
        self,
        method: str,
        path: str,
        params: dict[str, Any] | None = None,
        json: Any = None,
        allowed_status_codes: set[int] | None = None,
    ) -> httpx.Response:
        """Execute HTTP request with exponential backoff retry.

        Args:
            method: HTTP verb (GET, POST, etc.)
            path: Relative API path (e.g. '/repos/owner/repo/pulls')
            params: Optional query parameters.
            json: Optional JSON payload.
            allowed_status_codes: Set of non-2xx status codes considered valid (e.g. {404}).

        Returns:
            httpx.Response object.

        Raises:
            GitHubRateLimitError: If rate limited (429) after max retries.
            GitHubResourceNotFoundError: If 404 encountered and not in allowed_status_codes.
            GitHubAPIError: If request fails after retries.
        """
        if allowed_status_codes is None:
            allowed_status_codes = set()

        url = (
            path
            if path.startswith("http")
            else f"{self.base_url}{path if path.startswith('/') else '/' + path}"
        )
        last_exception: Exception | None = None

        for attempt in range(self.max_retries + 1):
            try:
                response = self._client.request(
                    method=method,
                    url=url,
                    params=params,
                    json=json,
                )

                if response.status_code in allowed_status_codes:
                    return response

                if response.status_code in RETRYABLE_STATUS_CODES:
                    if attempt < self.max_retries:
                        delay = self._calculate_backoff(attempt, response)
                        logger.warning(
                            "GitHub API returned %d for %s %s. Retrying in %.2f seconds (attempt %d/%d)...",
                            response.status_code,
                            method,
                            path,
                            delay,
                            attempt + 1,
                            self.max_retries,
                        )
                        time.sleep(delay)
                        continue
                    else:
                        if response.status_code == 429:
                            raise GitHubRateLimitError(
                                f"GitHub API rate limit exceeded after {self.max_retries} retries: {response.text}",
                                status_code=response.status_code,
                                response_body=response.text,
                            )
                        response.raise_for_status()

                if response.status_code == 404:
                    raise GitHubResourceNotFoundError(
                        f"Resource not found at {path}: {response.text}",
                        status_code=404,
                        response_body=response.text,
                    )

                response.raise_for_status()
                return response

            except (httpx.TransportError, httpx.TimeoutException) as exc:
                last_exception = exc
                if attempt < self.max_retries:
                    delay = self._calculate_backoff(attempt, None)
                    logger.warning(
                        "Network error (%s) contacting GitHub for %s %s. Retrying in %.2f seconds (attempt %d/%d)...",
                        type(exc).__name__,
                        method,
                        path,
                        delay,
                        attempt + 1,
                        self.max_retries,
                    )
                    time.sleep(delay)
                    continue
                logger.error(
                    "Transport error exhausted max retries for %s %s: %s", method, path, exc
                )
                raise GitHubAPIError(
                    f"Network error after {self.max_retries} retries: {exc}"
                ) from exc

            except httpx.HTTPStatusError as exc:
                logger.error(
                    "GitHub HTTP error %s for %s %s: %s",
                    exc.response.status_code,
                    method,
                    path,
                    exc.response.text,
                )
                raise GitHubAPIError(
                    f"GitHub API HTTP error {exc.response.status_code}: {exc.response.text}",
                    status_code=exc.response.status_code,
                    response_body=exc.response.text,
                ) from exc

        raise GitHubAPIError(f"Request to {path} failed after retries: {last_exception}")

    def _calculate_backoff(self, attempt: int, response: httpx.Response | None) -> float:
        """Calculate exponential backoff duration respecting Retry-After headers."""
        if response is not None:
            retry_after = response.headers.get("Retry-After")
            if retry_after:
                try:
                    return min(float(retry_after), 60.0)
                except ValueError:
                    pass

            # Check secondary rate limit reset header if present
            reset_header = response.headers.get("x-ratelimit-reset")
            if reset_header and response.status_code == 429:
                try:
                    wait_seconds = float(reset_header) - time.time()
                    if 0 < wait_seconds <= 60.0:
                        return wait_seconds
                except ValueError:
                    pass

        base_delay = self.backoff_factor * (2**attempt)
        jitter = random.uniform(0.0, 0.25 * base_delay)
        return min(base_delay + jitter, 60.0)

    def get_closed_prs(
        self,
        owner: str,
        repo: str,
        base_branch: str = "main",
        max_pages: int = 10,
    ) -> list[dict[str, Any]]:
        """Retrieve closed Pull Requests targeting base_branch.

        Args:
            owner: GitHub repository owner / organization.
            repo: GitHub repository name.
            base_branch: Target base branch to filter by (default 'main').
            max_pages: Maximum pagination depth to query.

        Returns:
            List of closed PR dictionaries.
        """
        all_prs: list[dict[str, Any]] = []
        path = f"/repos/{owner}/{repo}/pulls"

        for page in range(1, max_pages + 1):
            params = {
                "state": "closed",
                "base": base_branch,
                "sort": "updated",
                "direction": "desc",
                "per_page": 100,
                "page": page,
            }
            resp = self._request("GET", path, params=params)
            data = resp.json()
            if not isinstance(data, list) or not data:
                break

            all_prs.extend(data)
            if len(data) < 100:
                break

        return all_prs

    def get_open_prs(
        self,
        owner: str,
        repo: str,
        base_branch: str = "main",
    ) -> list[dict[str, Any]]:
        """Retrieve currently open Pull Requests targeting base_branch.

        Args:
            owner: GitHub repository owner / organization.
            repo: GitHub repository name.
            base_branch: Target base branch to filter by (default 'main').

        Returns:
            List of open PR dictionaries.
        """
        path = f"/repos/{owner}/{repo}/pulls"
        params = {
            "state": "open",
            "base": base_branch,
            "sort": "updated",
            "direction": "desc",
            "per_page": 100,
        }
        resp = self._request("GET", path, params=params)
        data = resp.json()
        return data if isinstance(data, list) else []

    def get_pr_details(self, owner: str, repo: str, pr_number: int) -> dict[str, Any]:
        """Retrieve detailed information for a specific Pull Request.

        Args:
            owner: Repository owner.
            repo: Repository name.
            pr_number: Pull request number.

        Returns:
            Dictionary containing PR details.
        """
        path = f"/repos/{owner}/{repo}/pulls/{pr_number}"
        resp = self._request("GET", path)
        return resp.json()

    def get_pr_commits(
        self,
        owner: str,
        repo: str,
        pr_number: int,
        max_pages: int = 5,
    ) -> list[dict[str, Any]]:
        """Retrieve commits for a specific PR with author and committer metadata.

        Args:
            owner: Repository owner.
            repo: Repository name.
            pr_number: Pull request number.
            max_pages: Maximum pagination depth.

        Returns:
            List of dictionaries with commit sha, commit message, author name,
            author email, author date, committer info, and raw commit data.
        """
        path = f"/repos/{owner}/{repo}/pulls/{pr_number}/commits"
        parsed_commits: list[dict[str, Any]] = []

        for page in range(1, max_pages + 1):
            params = {"per_page": 100, "page": page}
            resp = self._request("GET", path, params=params)
            data = resp.json()
            if not isinstance(data, list) or not data:
                break

            for item in data:
                sha = item.get("sha", "")
                commit_obj = item.get("commit") or {}
                message = commit_obj.get("message", "")
                author_obj = commit_obj.get("author") or {}
                committer_obj = commit_obj.get("committer") or {}

                # GitHub user account metadata if linked
                gh_author = item.get("author") or {}
                gh_committer = item.get("committer") or {}

                commit_info = {
                    "sha": sha,
                    "message": message,
                    "author_name": author_obj.get("name", ""),
                    "author_email": author_obj.get("email", ""),
                    "author_date": author_obj.get("date", ""),
                    "author_login": gh_author.get("login", ""),
                    "committer_name": committer_obj.get("name", ""),
                    "committer_email": committer_obj.get("email", ""),
                    "committer_date": committer_obj.get("date", ""),
                    "committer_login": gh_committer.get("login", ""),
                    "committer_info": committer_obj,
                    "raw": item,
                }
                parsed_commits.append(commit_info)

            if len(data) < 100:
                break

        return parsed_commits

    def get_pr_files(
        self,
        owner: str,
        repo: str,
        pr_number: int,
        max_pages: int = 5,
    ) -> list[str]:
        """Retrieve list of modified filenames for a specific Pull Request.

        Args:
            owner: Repository owner.
            repo: Repository name.
            pr_number: Pull request number.
            max_pages: Maximum pagination depth.

        Returns:
            List of changed file paths as strings.
        """
        path = f"/repos/{owner}/{repo}/pulls/{pr_number}/files"
        changed_files: list[str] = []

        for page in range(1, max_pages + 1):
            params = {"per_page": 100, "page": page}
            resp = self._request("GET", path, params=params)
            data = resp.json()
            if not isinstance(data, list) or not data:
                break

            for item in data:
                filename = item.get("filename")
                if filename:
                    changed_files.append(filename)

            if len(data) < 100:
                break

        return changed_files

    def check_pr_merged(self, owner: str, repo: str, pr_number: int) -> bool:
        """Check whether a Pull Request has been merged.

        Queries GitHub's merge endpoint:
        - HTTP 204: PR is merged -> True
        - HTTP 404: PR is not merged -> False

        Falls back to inspecting the PR details if an unexpected code is returned.

        Args:
            owner: Repository owner.
            repo: Repository name.
            pr_number: Pull request number.

        Returns:
            True if merged, False otherwise.
        """
        path = f"/repos/{owner}/{repo}/pulls/{pr_number}/merge"
        resp = self._request("GET", path, allowed_status_codes={204, 404})

        if resp.status_code == 204:
            return True
        if resp.status_code == 404:
            return False

        # Fallback inspection
        pr_data = self.get_pr_details(owner, repo, pr_number)
        return bool(pr_data.get("merged", False))

    def create_pull_request(
        self,
        owner: str,
        repo: str,
        title: str,
        head_branch: str,
        base_branch: str,
        body: str,
    ) -> dict[str, Any]:
        """Create a new Pull Request targeting base_branch.

        Args:
            owner: Target repository owner.
            repo: Target repository name.
            title: Pull request title.
            head_branch: Name of branch containing the changes.
            base_branch: Name of target branch (e.g. 'main').
            body: Markdown description body for the pull request.

        Returns:
            Dictionary containing the created pull request metadata.
        """
        path = f"/repos/{owner}/{repo}/pulls"
        payload = {
            "title": title,
            "head": head_branch,
            "base": base_branch,
            "body": body,
        }
        resp = self._request("POST", path, json=payload)
        return resp.json()

    def update_pull_request(
        self,
        owner: str,
        repo: str,
        pr_number: int,
        title: str | None = None,
        body: str | None = None,
    ) -> dict[str, Any]:
        """Update an existing Pull Request's title or description.

        Args:
            owner: Target repository owner.
            repo: Target repository name.
            pr_number: Pull request number.
            title: Optional updated title.
            body: Optional updated body description.

        Returns:
            Dictionary containing updated pull request metadata.
        """
        path = f"/repos/{owner}/{repo}/pulls/{pr_number}"
        payload: dict[str, Any] = {}
        if title is not None:
            payload["title"] = title
        if body is not None:
            payload["body"] = body

        resp = self._request("PATCH", path, json=payload)
        return resp.json()
