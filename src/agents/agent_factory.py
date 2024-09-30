# agents/agent_factory.py

import os
from crewai import Agent
from langchain_openai import ChatOpenAI
from src.agents import callback as callback_module  # Import the callback module
from src.utils.logger import logger
from src.tools.tool_factory import create_tool


def resolve_callback(callback_name):
    if callback_name:
        try:
            return getattr(callback_module, callback_name)
        except AttributeError:
            logger.error(f"Callback {callback_name} not found in callback module")
            return None
    return None

def create_agent(agent_config, tools_config):
    def get_tool_config(name):
        configs = tools_config["tools"]
        for config in configs:
            if config["name"] == name:
                return config

    tools = []
    for tool_name in agent_config["tools"]:
        tool_config = get_tool_config(tool_name)
        if not tool_config:
            logger.error(f"Tool {tool_name} doesn't exist")
        else:
            tool = create_tool(tool_config)
            if tool:
                logger.info(f'Got tool: {tool_name}')
                logger.info(f'Tool details: {tool.__dict__}')
                tools.append(tool)
            else:
                logger.error(f"Tool {tool_name} doesn't exist")

    logger.info(f'Got Tools for agent {agent_config["role"]}: {tools}')

    # Ensure an LLM model is specified
    llm_model = agent_config.get("llm", "gpt-3.5-turbo")  # Default to gpt-3.5-turbo if not specified

    # Initialize the LLM
    llm = ChatOpenAI(model=llm_model)

    # Resolve step callback
    step_callback = resolve_callback(agent_config.get("step_callback"))

    try:
        agent = Agent(
            role=agent_config["role"],
            goal=agent_config["goal"],
            verbose=agent_config["verbose"],
            memory=agent_config.get("memory", False),
            backstory=agent_config["backstory"],
            tools=tools,
            llm=llm,
            function_calling_llm=ChatOpenAI(model=agent_config.get("function_calling_llm", "gpt-4")),
            max_iter=agent_config.get("max_iter", 25),
            max_rpm=agent_config.get("max_rpm"),
            max_execution_time=agent_config.get("max_execution_time"),
            allow_delegation=agent_config["allow_delegation"],
            step_callback=step_callback,  # Use the resolved function
            cache=agent_config.get("cache", True),
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        logger.info(f'Created agent: {agent_config["role"]} with tools: {tools}')
        logger.info(f'Using LLM for agent {agent_config["role"]}: {llm.model_name}')
        return agent
    except Exception as e:
        logger.error(f'Error creating agent {agent_config["role"]}: {e}')
        logger.error(f'Agent config: {agent_config}')
        logger.error(f'Tools: {tools}')
        raise e
