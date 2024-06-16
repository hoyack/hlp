# main.py

import os
import sys
import logging
import time
from dotenv import load_dotenv
from crewai import Crew, Process
from utils.json_loader import load_json
from agents.agent_factory import create_agent
from tasks.task_factory import create_task

# Configure logger
logger = logging.getLogger('main_logger')
logger.setLevel(logging.INFO)

# Create log directory if it doesn't exist
if not os.path.exists('log'):
    os.makedirs('log')

# Create file handler with a unique log file name
log_file = os.path.join('log', f'{int(time.time())}.log')
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)

class LoggerWriter:
    def __init__(self, logger, level):
        self.logger = logger
        self.level = level

    def write(self, message):
        if message.strip() != "":
            self.logger.log(self.level, message)

    def flush(self):
        pass

# Load environment variables from .env file
load_dotenv()

def main():
    idea = input("Enter your business idea: ")

    # Redirect stdout to logger
    sys.stdout = LoggerWriter(logger, logging.INFO)
    sys.stderr = LoggerWriter(logger, logging.ERROR)

    # Load configurations
    agents_config = load_json('src/templates/agents_config.json')
    tasks_config = load_json('src/templates/tasks_config.json')

    # Create agents
    agents = {config["role"]: create_agent(config) for config in agents_config["agents"]}

    # Create tasks with the idea_summary
    tasks = [create_task(config, agents, idea) for config in tasks_config["tasks"]]

    # Assemble the crew
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential,
        memory=True,
        cache=True,
        max_rpm=100,
        share_crew=True
    )

    logger.info('Crew assembled and kickoff initiated')

    # Kick off the crew
    result = crew.kickoff()
    logger.info('Crew execution completed')
    logger.info(f'Result: {result}')

if __name__ == "__main__":
    main()
