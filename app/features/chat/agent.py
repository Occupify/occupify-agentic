from pydantic_ai import Agent

from app.agents.deps import AgentDeps
from app.features.chat.prompts import CHAT_SYSTEM_PROMPT
from app.llm.glm import model_for


def get_chat_agent() -> Agent[AgentDeps, str]:
    model = model_for("chat")
    agent = Agent(
        model=model,
        system_prompt=CHAT_SYSTEM_PROMPT,
        deps_type=AgentDeps,
    )
    return agent


chat_agent = get_chat_agent()
