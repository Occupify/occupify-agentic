import logging

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import JobIndexRow

logger = logging.getLogger(__name__)


async def sweep_job_index(session: AsyncSession, seen_job_ids: list[str]) -> None:
    """Sweeps job index against newly seen job IDs from core.

    Increments missed_sweeps for jobs not present in seen_job_ids.
    Deactivates jobs (active = False) when missed_sweeps >= 2.
    Resets missed_sweeps to 0 for seen jobs.
    """
    seen_set = set(seen_job_ids)
    stmt = select(JobIndexRow).where(JobIndexRow.active.is_(True))
    result = await session.execute(stmt)
    rows = result.scalars().all()

    for row in rows:
        if row.job_id not in seen_set:
            row.missed_sweeps += 1
            if row.missed_sweeps >= 2:
                row.active = False
                logger.info(
                    "Deactivated job %s after %d missed sweeps", row.job_id, row.missed_sweeps
                )
        else:
            row.missed_sweeps = 0

    await session.commit()
