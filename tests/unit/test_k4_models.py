from app.db.models import CvImprovementSession, TaskCheckpoint, UserMemory


def test_user_memory_model():
    """Verify UserMemory schema, columns, constraints and indexes."""
    assert UserMemory.__tablename__ == "user_memory"

    columns = {c.name: c for c in UserMemory.__table__.columns}
    expected_cols = [
        "id",
        "user_id",
        "category",
        "key",
        "value",
        "is_confirmed",
        "confidence",
        "source",
        "created_at",
        "updated_at",
        "expires_at",
    ]
    for col in expected_cols:
        assert col in columns, f"Missing column {col} in UserMemory"

    # Unique constraint across user_id, category, key
    uq_names = [
        c
        for c in UserMemory.__table__.constraints
        if getattr(c, "name", None) == "uq_user_memory_key"
    ]
    assert len(uq_names) == 1
    assert {c.name for c in uq_names[0].columns} == {"user_id", "category", "key"}

    # Index check
    index_names = {idx.name for idx in UserMemory.__table__.indexes}
    assert "ix_user_memory_user_category" in index_names


def test_task_checkpoint_model():
    """Verify TaskCheckpoint schema, columns and indexes."""
    assert TaskCheckpoint.__tablename__ == "task_checkpoints"

    columns = {c.name: c for c in TaskCheckpoint.__table__.columns}
    expected_cols = [
        "id",
        "session_id",
        "user_id",
        "task_type",
        "stage",
        "goal",
        "constraints",
        "completed_steps",
        "pending_steps",
        "blockers",
        "decisions",
        "next_action",
        "checkpoint_seq",
        "created_at",
    ]
    for col in expected_cols:
        assert col in columns, f"Missing column {col} in TaskCheckpoint"

    index_names = {idx.name for idx in TaskCheckpoint.__table__.indexes}
    assert "ix_task_checkpoints_session_seq" in index_names
    assert "ix_task_checkpoints_user_task" in index_names


def test_cv_improvement_session_model():
    """Verify CvImprovementSession schema, columns, defaults and indexes."""
    assert CvImprovementSession.__tablename__ == "cv_improvement_sessions"

    columns = {c.name: c for c in CvImprovementSession.__table__.columns}
    expected_cols = [
        "id",
        "user_id",
        "chat_session_id",
        "status",
        "original_cv_text",
        "target_jd_text",
        "proposals",
        "user_decisions",
        "revised_resume_data",
        "pdf_url",
        "created_at",
        "updated_at",
    ]
    for col in expected_cols:
        assert col in columns, f"Missing column {col} in CvImprovementSession"

    # chat_session_id must be nullable
    assert columns["chat_session_id"].nullable is True

    # Index checks
    index_names = {idx.name for idx in CvImprovementSession.__table__.indexes}
    assert "ix_cv_improvement_sessions_user_id" in index_names
    assert "ix_cv_improvement_sessions_chat_session_id" in index_names
    assert "ix_cv_improvement_sessions_user_updated" in index_names

