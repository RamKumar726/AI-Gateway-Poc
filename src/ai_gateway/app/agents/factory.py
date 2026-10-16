from langchain.agents import create_agent


def build_agent(model, tools, system_prompt):
    return create_agent(
        model = model,
        tools = tools,
        system_prompt= system_prompt
    )