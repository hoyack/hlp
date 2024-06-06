from crewai import Task
from textwrap import dedent

def create_review_problem_task(agent, identified_problems):
    """
    Create a task for reviewing identified problem statements.
    
    :param agent: The agent responsible for the task.
    :param identified_problems: The statements of problems identified to be reviewed.
    :return: A Task instance for problem review.
    """
    return Task(description=dedent(f"""
        Review the identified problem statements:
        "{identified_problems}". 
        Verify the accuracy and relevance of the problem statements 
        and provide constructive feedback for improvement.
      """),
      agent=agent
    )
