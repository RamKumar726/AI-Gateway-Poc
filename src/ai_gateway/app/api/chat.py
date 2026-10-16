from fastapi import FastAPI, HTTPException
from langchain_core.messages import HumanMessage, SystemMessage
from pydantic import BaseModel, Field

from ..personas.loader import load_persona
from ..models.factory import build_model
from ..agents.factory import build_agent
from ..tools.tool_registry import load_tool

def chat(question, persona_id):
    persona = load_persona(persona_id=persona_id)
    system_prompt = persona['system_prompt']
    llm_model = build_model(persona)
    tool_names = persona['tools']
    tools = load_tool(tool_names=tool_names)
    agent = build_agent(model = llm_model, tools = tools, system_prompt=system_prompt )
    result = agent.invoke(
        {
            "messages" : [HumanMessage(content = question)]
        }
    )

    return result


res = chat("Hey Hi. What are the product details of P101?", "enen")
print(res['messages'][-1].content)
