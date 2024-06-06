from crewai import Crew
from agents.manager import Manager
from agents.problem_assessor import ProblemAssessor
from agents.problem_reviewer import ProblemReviewer
from tasks.assess_problem import create_assess_problem_task
from tasks.review_problem import create_review_problem_task

from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class LeanCanvasCrew:
    """
    Class to manage the Lean Canvas Crew operations.
    """

    def __init__(self, idea_summary):
        """
        Initialize with the summary of the brilliant idea.
        
        :param idea_summary: A brief description of the idea to be assessed.
        """
        self.idea_summary = idea_summary

    def run(self):
        """
        Run the Lean Canvas Crew operations.
        
        :return: The result of the crew operations.
        """
        # Initialize the manager
        manager = Manager()

        # Create agents for problem assessment and review
        problem_assessor_agent = ProblemAssessor(manager).to_agent()
        problem_reviewer_agent = ProblemReviewer().to_agent()

        # Create tasks for problem assessment and review
        identify_task = create_assess_problem_task(
            problem_assessor_agent,
            self.idea_summary
        )
        review_task = create_review_problem_task(
            problem_reviewer_agent,
            self.idea_summary
        )

        # Initialize the Crew with agents and tasks
        crew = Crew(
            agents=[
                problem_assessor_agent, problem_reviewer_agent
            ],
            tasks=[identify_task, review_task],
            verbose=True
        )

        # Kick off the crew operations and return the result
        result = crew.kickoff()
        return result

if __name__ == "__main__":
    idea_summary = input("Enter the summary of the brilliant idea: ")

    # Create and run the Lean Canvas Crew with the provided idea summary
    lean_canvas_crew = LeanCanvasCrew(idea_summary)
    result = lean_canvas_crew.run()

    print("\n\n########################")
    print("## Here is your Lean Canvas Problem Assessment")
    print("########################\n")
    print(result)
