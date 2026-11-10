"""Unit and integration tests for SyncEngine CLI."""

from unittest.mock import MagicMock, patch

import pytest
from sync_engine import db
from sync_engine.cli import main


@pytest.fixture(autouse=True)
def setup_isolated_db(tmp_path, monkeypatch):
    """Provide an isolated SQLite database for each test."""
    db_file = tmp_path / "cli_test.db"
    db_url = f"sqlite:///{db_file}"
    monkeypatch.setenv("DATABASE_URL", db_url)
    monkeypatch.setenv("SYNC_DATABASE_URL", db_url)
    db.init_db(db_url)
    yield db_url
    db._engine = None
    db._sessionmaker = None


def test_cli_help():
    """Verify CLI --help exits with code 0."""
    with pytest.raises(SystemExit) as exc:
        main(["--help"])
    assert exc.value.code == 0


def test_cli_no_args_exits_cleanly(capsys):
    """Verify running CLI without arguments prints help and exits 0."""
    code = main([])
    assert code == 0
    captured = capsys.readouterr()
    assert "usage:" in captured.out or "Occupify" in captured.out


def test_cli_invalid_command():
    """Verify invalid subcommand returns error code 2 from argparse."""
    with pytest.raises(SystemExit) as exc:
        main(["nonexistent-command"])
    assert exc.value.code != 0


def test_cli_init_db(setup_isolated_db, capsys):
    """Verify init-db subcommand initializes tables and exits 0."""
    db_url = setup_isolated_db
    code = main(["init-db", "--db-url", db_url])
    assert code == 0
    captured = capsys.readouterr()
    assert "Database tables initialized successfully" in captured.out


def test_cli_status(setup_isolated_db, capsys):
    """Verify status subcommand prints status report."""
    db_url = setup_isolated_db
    code = main(["status", "--db-url", db_url])
    assert code == 0
    captured = capsys.readouterr()
    assert "Occupify Contribution Sync Engine - Status Report" in captured.out
    assert "[Checkpoint]" in captured.out
    assert "[Active Sync Lock]" in captured.out


@patch("sync_engine.cli.SyncEngine")
def test_cli_stage_commands(mock_engine_cls, setup_isolated_db, capsys):
    """Verify individual stage subcommands invoke corresponding engine methods."""
    mock_instance = MagicMock()
    mock_engine_cls.return_value = mock_instance

    mock_instance.stage1_checkout_source.return_value = "sha_111"
    mock_instance.stage2_load_checkpoint.return_value = MagicMock(
        initial_checkpoint_sha="sha_baseline"
    )
    mock_instance.stage3_find_new_prs.return_value = [{"number": 10, "title": "Test PR"}]
    mock_instance.stage4_extract_contributions.return_value = MagicMock(
        source_pr_number=10, contributors=[], changed_files=[]
    )
    mock_instance.stage5_calculate_diff.return_value = "patch diff content"
    mock_instance.stage6_sync_target.return_value = (True, None)
    mock_instance.stage7_create_pr.return_value = {
        "number": 55,
        "html_url": "https://github.com/Occupify/pull/55",
    }

    db_url = setup_isolated_db

    # Stage 1
    assert main(["checkout-source", "--db-url", db_url]) == 0
    mock_instance.stage1_checkout_source.assert_called_once()

    # Stage 2
    assert main(["load-checkpoint", "--db-url", db_url]) == 0
    mock_instance.stage2_load_checkpoint.assert_called_once()

    # Stage 3
    assert main(["find-prs", "--db-url", db_url]) == 0
    mock_instance.stage3_find_new_prs.assert_called_once()

    # Stage 4
    with patch("sync_engine.cli._get_target_contribution") as mock_get_rec:
        mock_rec = MagicMock(source_pr_number=10)
        mock_get_rec.return_value = mock_rec
        assert main(["extract-contributions", "--db-url", db_url]) == 0
        mock_instance.stage4_extract_contributions.assert_called_once()

    # Stage 5
    with patch("sync_engine.cli._get_target_contribution") as mock_get_rec:
        mock_rec = MagicMock(source_pr_number=10)
        mock_get_rec.return_value = mock_rec
        assert main(["calculate-diff", "--db-url", db_url]) == 0
        mock_instance.stage5_calculate_diff.assert_called_once()

    # Stage 6
    with patch("sync_engine.cli._get_target_contribution") as mock_get_rec:
        mock_rec = MagicMock(source_pr_number=10, sync_branch="sync/b/pr-10")
        mock_get_rec.return_value = mock_rec
        assert main(["sync-target", "--db-url", db_url]) == 0
        mock_instance.stage6_sync_target.assert_called_once()

    # Stage 7
    with patch("sync_engine.cli._get_target_contribution") as mock_get_rec:
        mock_rec = MagicMock(source_pr_number=10)
        mock_get_rec.return_value = mock_rec
        assert main(["create-pr", "--db-url", db_url]) == 0
        mock_instance.stage7_create_pr.assert_called_once()

    # Stage 8
    with patch("sync_engine.cli._get_target_contribution") as mock_get_rec:
        mock_rec = MagicMock(source_pr_number=10, sync_key="PR_10")
        mock_get_rec.return_value = mock_rec
        assert main(["update-state", "--db-url", db_url]) == 0
        mock_instance.stage8_update_state.assert_called_once()


@patch("sync_engine.cli.SyncEngine")
def test_cli_run_all_dry_run(mock_engine_cls, setup_isolated_db, capsys):
    """Verify run-all subcommand with --dry-run invokes run_all and exits 0."""
    mock_instance = MagicMock()
    mock_engine_cls.return_value = mock_instance
    mock_instance.run_all.return_value = {
        "status": "SUCCESS",
        "message": "Successfully synchronized 1 PR(s)",
        "synced_prs": [{"source_pr": 10, "destination_pr": 9999}],
    }

    db_url = setup_isolated_db
    code = main(["run-all", "--dry-run", "--db-url", db_url])
    assert code == 0
    mock_instance.run_all.assert_called_once()
    captured = capsys.readouterr()
    assert "Pipeline Result: SUCCESS" in captured.out


@patch("sync_engine.cli.SyncEngine")
def test_cli_run_all_conflict_exits_nonzero(mock_engine_cls, setup_isolated_db, capsys):
    """Verify run-all exits with code 1 when conflict status is encountered."""
    mock_instance = MagicMock()
    mock_engine_cls.return_value = mock_instance
    mock_instance.run_all.return_value = {
        "status": "CONFLICT",
        "pr_number": 99,
        "error": "Merge conflict in index.html",
        "synced_prs": [],
    }

    db_url = setup_isolated_db
    code = main(["run-all", "--db-url", db_url])
    assert code == 1
    captured = capsys.readouterr()
    assert "Halting on conflict for PR #99" in captured.err
