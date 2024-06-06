from tasks.assess_problem import create_assess_problem_task
from tasks.review_problem import create_review_problem_task

class Manager:
    """
    Manager class to assign tasks to agents.
    """

    def assign_problem_assessor(self, idea_summary):
        """
        Assign the problem assessment task to the Problem Assessor agent.
        
        :param idea_summary: A brief description of the idea to be assessed.
        """
        create_assess_problem_task(idea_summary, self)

    def assign_problem_reviewer(self, problem_statements):
        """
        Assign the problem review task to the Problem Reviewer agent.
        
        :param problem_statements: The statements of problems identified to be reviewed.
        """
        create_review_problem_task(problem_statements)
