# tasks/task_factory.py
from crewai import Task
from src.utils.logger import logger

def create_task(task_config, agents, idea_summary):
    """
    Create a task based on the task configuration and assigned agents.

    Args:
        task_config (dict): The configuration for the task.
        agents (dict): A dictionary of agents.
        idea_summary (str): The summary of the business idea.

    Returns:
        Task: The created task instance.
    """
    agent = agents[task_config["role"]]

    # Prepare the parameters for the Task constructor
    task_params = {
        "description": f"{task_config['description']} for {idea_summary}",
        "agent": agent,
        "expected_output": task_config.get("expected_output", ""),
        "tools": agent.tools,
        "async_execution": task_config.get("async_execution", False),
        "context": task_config.get("context", []),
        "config": task_config.get("config", {}),
        "callback": task_config.get("callback", None),
        "human_input": task_config.get("human_input", False)
    }

    # Handle output_json, output_pydantic, and output_file correctly
    if isinstance(task_config.get("output_json"), dict):
        task_params["output_json"] = task_config["output_json"]
    if isinstance(task_config.get("output_pydantic"), dict):
        task_params["output_pydantic"] = task_config["output_pydantic"]
    if isinstance(task_config.get("output_file"), str):
        task_params["output_file"] = task_config["output_file"]

    task = Task(**task_params)
    
    logger.info(f'Created task: {task_config["name"]} for agent: {task_config["role"]}')
    return task
