from crewai import Agent

class ProblemReviewer:
    def review_problem(self, problem_statements):
        # Review problem statements and provide feedback
        problem_data = problem_statements.get("problem_statements", [])
        for problem in problem_data:
            print(f"Reviewing problem: {problem.get('title', 'No title')}")
            # Add feedback process here

        print("Problem review completed. Feedback provided.")

    def to_agent(self):
        return Agent(
            role='Problem Reviewer',
            goal='Review the identified problems and provide feedback for improvements.',
            backstory='An expert in reviewing and refining problem statements.',
            tools=[],
            verbose=True
        )
