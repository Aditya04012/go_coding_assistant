from langchain.agents import create_agent
from agent.llm import llm
from agent.prompts import SYSTEM_PROMPT
from agent.tool import tools


assistant=create_agent(
    model=llm,
    tools=tools,
    system_prompt=SYSTEM_PROMPT
)