import os
import sys
import logging
import time
from dotenv import load_dotenv
from crewai import Crew, Process
from langchain_openai import ChatOpenAI
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

def instantiate_crews(crews_config, agents_config, tasks_config, idea):
    previous_output = idea
    for crew_config in crews_config["crews"]:
        logger.info(f'Instantiating crew: {crew_config["name"]}')

        # Create agents for the crew
        agents = {agent_config["role"]: create_agent(agent_config) 
                  for agent_config in agents_config["agents"] 
                  if agent_config["role"] in crew_config["agents"]}

        # Create tasks for the crew
        tasks = [create_task(task_config, agents, previous_output) 
                 for task_config in tasks_config["tasks"] 
                 if task_config["name"] in crew_config["tasks"]]

        # Set up the process
        process = Process.sequential if crew_config["process"] == "sequential" else Process.hierarchical
        manager_llm = None
        if process == Process.hierarchical and "manager_llm" in crew_config:
            manager_llm = ChatOpenAI(model=crew_config["manager_llm"])

        # Assemble the crew
        crew = Crew(
            agents=list(agents.values()),
            tasks=tasks,
            process=process,
            manager_llm=manager_llm,
            verbose=crew_config.get("verbose", False),
            config=crew_config.get("config", {}),
            max_rpm=crew_config.get("max_rpm"),
            language=crew_config.get("language", "en"),
            memory=crew_config.get("memory", False),
            cache=crew_config.get("cache", True),
            embedder=crew_config.get("embedder"),
            full_output=crew_config.get("full_output", False),
            step_callback=crew_config.get("step_callback"),
            task_callback=crew_config.get("task_callback"),
            share_crew=crew_config.get("share_crew", False),
            output_log_file=crew_config.get("output_log_file")
        )

        logger.info(f'Crew {crew_config["name"]} assembled and kickoff initiated')

        # Kick off the crew
        result = crew.kickoff()
        logger.info(f'Crew {crew_config["name"]} execution completed')
        logger.info(f'Result: {result}')

        # Use the output of the current crew as the input for the next crew
        previous_output = result

    return previous_output

def main():
    idea = input("Enter your business idea: ")

    # Redirect stdout to logger
    sys.stdout = LoggerWriter(logger, logging.INFO)
    sys.stderr = LoggerWriter(logger, logging.ERROR)

    # Load configurations
    crews_config = load_json('src/templates/crews_config.json')
    agents_config = load_json('src/templates/agents_config.json')
    tasks_config = load_json('src/templates/tasks_config.json')

    # Instantiate and run crews
    final_output = instantiate_crews(crews_config, agents_config, tasks_config, idea)
    logger.info(f'Final output: {final_output}')

if __name__ == "__main__":
    main()
