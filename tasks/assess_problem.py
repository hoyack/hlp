from crewai import Task
from textwrap import dedent

def create_assess_problem_task(agent, idea_summary):
    """
    Create a task for assessing problems related to the idea summary.
    
    :param agent: The agent responsible for the task.
    :param idea_summary: A brief description of the idea to be assessed.
    :return: A Task instance for problem assessment.
    """
    return Task(description=dedent(f"""
        Analyze and identify the core problems related to the idea: 
        "{idea_summary}". 
        Use internet searches and website content scraping to gather 
        information about market pain points and existing solutions. 
        Summarize your findings into clear problem statements.
      """),
      agent=agent
    )
