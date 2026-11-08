from pydantic_ai import Agent

from app.agents.deps import AgentDeps
from app.agents.subagent import invoke_subagent
from app.features.career_rag.chat_tool import consult_career_knowledge
from app.features.chat.prompts import CHAT_SYSTEM_PROMPT
from app.features.job_match.chat_tool import match_jobs_for_cv
from app.features.projects.tools import get_project_detail, search_filter_projects
from app.llm.glm import get_model


def get_chat_agent() -> Agent[AgentDeps, str]:
    model = get_model()
    agent = Agent(
        model=model,
        system_prompt=CHAT_SYSTEM_PROMPT,
        deps_type=AgentDeps,
    )
    agent.tool(search_filter_projects)
    agent.tool(get_project_detail)
    agent.tool(invoke_subagent)
    agent.tool(match_jobs_for_cv)
    agent.tool(consult_career_knowledge)
    return agent


chat_agent = get_chat_agent()
