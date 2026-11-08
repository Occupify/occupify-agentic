import logging

from pydantic_ai import RunContext

from app.agents.deps import AgentDeps
from app.db.session import get_sessionmaker
from app.features.career_rag.service import CareerConsultantService

logger = logging.getLogger(__name__)


async def consult_career_knowledge(
    ctx: RunContext[AgentDeps],
    query: str,
    domain: str | None = None,
    source_type: str | None = None,
) -> str:
    """Tra cứu cơ sở tri thức nghề nghiệp chuẩn hóa (Roadmaps, ESCO taxonomy, O*NET competencies).

    Sử dụng công cụ này khi người dùng hỏi về:
    - Lộ trình học tập hoặc phát triển nghề nghiệp (ví dụ: roadmap Backend, Frontend, DevOps...).
    - Tiêu chuẩn nghề nghiệp, định nghĩa vị trí công việc, hoặc bộ kỹ năng theo chuẩn quốc tế (ESCO, O*NET).
    - Phân tích kỹ năng cốt lõi cho một ngành hoặc chức danh.

    KHÔNG dùng công cụ này để tìm việc cho CV cá nhân (hãy dùng `match_jobs_for_cv`) hoặc tìm dự án freelance cụ thể trên sàn (hãy dùng `search_filter_projects`).
    """
    db_session = ctx.deps.db

    # If DB session is provided in deps, use it directly
    if db_session is not None:
        service = CareerConsultantService(session=db_session)
        resp = await service.consult(
            query=query,
            domain=domain,
            source_type=source_type,
        )
        return resp.answer

    # Otherwise open a managed DB session from engine
    maker = get_sessionmaker()
    async with maker() as session:
        service = CareerConsultantService(session=session)
        resp = await service.consult(
            query=query,
            domain=domain,
            source_type=source_type,
        )
        return resp.answer
