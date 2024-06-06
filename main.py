from crewai import Crew
from agents.manager import Manager
from agents.problem_assessor import ProblemAssessor
from agents.problem_reviewer import ProblemReviewer
from tasks.assess_problem import create_assess_problem_task
from tasks.review_problem import create_review_problem_task

from dotenv import load_dotenv
load_dotenv()

class LeanCanvasCrew:

  def __init__(self, idea_summary):
    self.idea_summary = idea_summary

  def run(self):
    manager = Manager()

    problem_assessor_agent = ProblemAssessor(manager).to_agent()
    problem_reviewer_agent = ProblemReviewer().to_agent()

    identify_task = create_assess_problem_task(
      problem_assessor_agent,
      self.idea_summary
    )
    review_task = create_review_problem_task(
      problem_reviewer_agent,
      self.idea_summary
    )

    crew = Crew(
      agents=[
        problem_assessor_agent, problem_reviewer_agent
      ],
      tasks=[identify_task, review_task],
      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  idea_summary = input("Enter the summary of the brilliant idea: ")
  
  lean_canvas_crew = LeanCanvasCrew(idea_summary)
  result = lean_canvas_crew.run()
  print("\n\n########################")
  print("## Here is your Lean Canvas Problem Assessment")
  print("########################\n")
  print(result)
