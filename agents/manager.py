from tasks.assess_problem import create_assess_problem_task
from tasks.review_problem import create_review_problem_task

class Manager:
    def assign_problem_assessor(self, idea_summary):
        create_assess_problem_task(idea_summary, self)

    def assign_problem_reviewer(self, problem_statements):
        create_review_problem_task(problem_statements)
