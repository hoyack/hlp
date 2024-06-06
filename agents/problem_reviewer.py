from crewai import Agent

class ProblemReviewer:
    """
    Problem Reviewer class to review identified problem statements.
    """

    def review_problem(self, problem_statements):
        """
        Review the problem statements and provide feedback.
        
        :param problem_statements: The statements of problems identified to be reviewed.
        """
        problem_data = problem_statements.get("problem_statements", [])
        for problem in problem_data:
            print(f"Reviewing problem: {problem.get('title', 'No title')}")
            # Add feedback process here

        print("Problem review completed. Feedback provided.")

    def to_agent(self):
        """
        Convert the Problem Reviewer instance to an Agent instance.
        
        :return: An Agent instance configured for problem review.
        """
        return Agent(
            role='Problem Reviewer',
            goal='Review the identified problems and provide feedback for improvements.',
            backstory='An expert in reviewing and refining problem statements.',
            tools=[],
            verbose=True
        )
