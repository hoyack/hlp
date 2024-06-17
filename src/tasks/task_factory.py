# tasks/task_factory.py
from crewai import Task
from utils.logger import logger

def create_task(task_config, agents, idea_summary):
    try:
        agent = agents[task_config["role"]]
        task = Task(
            description=f"{task_config['description']} for {idea_summary}",
            expected_output='',
            tools=agent.tools,
            agent=agent,
            async_execution=task_config.get("async_execution", False)
        )
        logger.info(f'Created task: {task_config["description"]} for agent: {task_config["role"]}')
        return task
    except KeyError as e:
        logger.error(f'Missing key in task configuration: {e}')
        raise e
