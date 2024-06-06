from crewai import Task
from textwrap import dedent

def create_assess_problem_task(agent, idea_summary):
    return Task(description=dedent(f"""
        Analyze and identify the core problems related to the idea: 
        "{idea_summary}". 
        Use internet searches and website content scraping to gather 
        information about market pain points and existing solutions. 
        Summarize your findings into clear problem statements.
      """),
      agent=agent
    )
