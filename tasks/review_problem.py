from crewai import Task
from textwrap import dedent

def create_review_problem_task(agent, identified_problems):
    return Task(description=dedent(f"""
        Review the identified problem statements:
        "{identified_problems}". 
        Verify the accuracy and relevance of the problem statements 
        and provide constructive feedback for improvement.
      """),
      agent=agent
    )
