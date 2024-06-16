# agents/agent_factory.py

import os
import json
import importlib
from crewai import Agent
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI
from utils.logger import logger

def load_tool_mapping(file_path):
    with open(file_path, 'r') as file:
        tool_mapping = json.load(file)
    loaded_tools = {}
    for tool_name, tool_path in tool_mapping.items():
        module_name, class_name = tool_path.split(':')
        module = importlib.import_module(module_name)
        tool_class = getattr(module, class_name)
        loaded_tools[tool_name] = tool_class
    return loaded_tools

tool_mapping = load_tool_mapping('src/templates/tools_config.json')

def create_agent(agent_config):
    tools = []
    for tool_name in agent_config["tools"]:
        tool_class = tool_mapping.get(tool_name)
        if tool_class:
            try:
                tool_instance = tool_class()
                tools.append(tool_instance)
                logger.info(f'Instantiated tool: {tool_name}')
                logger.info(f'Tool details: {tool_instance.__dict__}')
            except Exception as e:
                logger.error(f'Error instantiating tool {tool_name}: {e}')
        else:
            logger.error(f'Tool {tool_name} not found in tool_mapping')

    logger.info(f'Tools instantiated for agent {agent_config["role"]}: {tools}')

    # Ensure an LLM model is specified
    if "llm" not in agent_config:
        raise ValueError(f'LLM model must be specified for agent: {agent_config["role"]}')

    # Initialize the LLM
    llm = ChatOpenAI(model=agent_config["llm"])

    try:
        agent = Agent(
            role=agent_config["role"],
            goal=agent_config["goal"],
            verbose=agent_config["verbose"],
            memory=agent_config.get("memory", False),
            backstory=agent_config["backstory"],
            tools=tools,
            llm=llm,
            allow_delegation=agent_config["allow_delegation"],
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
