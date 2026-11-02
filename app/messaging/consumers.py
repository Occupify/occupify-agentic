import logging
from typing import Any

from faststream.rabbit.annotations import RabbitMessage

from app.core.logging import log_step
from app.db.session import get_sessionmaker
from app.features.job_match.index.store import delete_job_by_id, delete_jobs_by_project
from app.features.job_match.index.sync import sync_single_project
from app.messaging.broker import get_broker
from app.messaging.core_client import get_core_rpc
from app.messaging.topology import events_exchange, job_item_queue, job_sync_queue

logger = logging.getLogger(__name__)
broker = get_broker()


@broker.subscriber(queue=job_sync_queue, exchange=events_exchange)
async def handle_project_event(
    message: dict[str, Any], raw_message: RabbitMessage
) -> None:
    """
    Handles project.* events from RabbitMQ (created, updated, status_changed, deleted).
    Re-sanitizes, re-embeds, and updates job_index.
    """
    raw = getattr(raw_message, "raw_message", raw_message)
    routing_key = getattr(raw, "routing_key", "") or "project.updated"
    logger.info("Received project event [%s]", routing_key)

    project_id = str(message.get("id") or message.get("projectId") or "")

    # Deletion or closure
    status = str(message.get("status") or "").upper()
    if routing_key in ("project.deleted", "project.closed") or status in (
        "CLOSED",
        "CANCELLED",
        "ARCHIVED",
    ):
        if project_id:
            session_maker = get_sessionmaker()
            async with session_maker() as session:
                deleted = await delete_jobs_by_project(session, project_id)
                log_step("job_sync.event_project_deleted", project_id=project_id, deleted=deleted)
        return

    # Project created or updated: resolve full data
    project_data = message.get("data") or message
    if not project_data.get("jobs") and project_id:
        core_rpc = get_core_rpc()
        try:
            reply = await core_rpc.call("core.project.get", {"projectId": project_id})
            if reply and reply.get("ok"):
                project_data = reply.get("data") or {}
        except Exception as exc:
            logger.warning("Failed to fetch project %s from core_rpc: %s", project_id, exc)

    if project_data and isinstance(project_data, dict):
        await sync_single_project(project_data)


@broker.subscriber(queue=job_item_queue, exchange=events_exchange)
async def handle_job_event(
    message: dict[str, Any], raw_message: RabbitMessage
) -> None:
    """
    Handles job.* events from RabbitMQ (created, updated, closed, deleted).
    """
    raw = getattr(raw_message, "raw_message", raw_message)
    routing_key = getattr(raw, "routing_key", "") or "job.updated"
    logger.info("Received job event [%s]", routing_key)

    job_id = str(message.get("id") or message.get("jobId") or "")
    project_id = str(message.get("projectId") or message.get("project_id") or "")
    status = str(message.get("newStatus") or message.get("status") or "").upper()

    if routing_key in ("job.deleted", "job.closed") or status in ("CLOSED", "FILLED"):
        if job_id:
            session_maker = get_sessionmaker()
            async with session_maker() as session:
                await delete_job_by_id(session, job_id)
                log_step("job_sync.event_job_deleted", job_id=job_id)
        return

    # Re-sync parent project if available
    if project_id:
        core_rpc = get_core_rpc()
        try:
            reply = await core_rpc.call("core.project.get", {"projectId": project_id})
            if reply and reply.get("ok"):
                p_data = reply.get("data") or {}
                await sync_single_project(p_data)
        except Exception as exc:
            logger.warning("Failed to refresh project %s after job event: %s", project_id, exc)
