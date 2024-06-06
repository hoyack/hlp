from tools.browserless_tool import BrowserTools
from tools.serper_tool import SearchTools
from crewai import Agent

class ProblemAssessor:
    """
    Problem Assessor class to identify and summarize the core problems of an idea.
    """

    def __init__(self, manager):
        """
        Initialize with a manager instance.
        
        :param manager: An instance of the Manager class.
        """
        self.manager = manager

    def assess_problem(self, idea_summary):
        """
        Assess the problems related to the provided idea summary.
        
        :param idea_summary: A brief description of the idea to be assessed.
        """
        # Use Serper to perform a search for pain points
        search_results = SearchTools.search_internet(f"pain points in {idea_summary}")
        problem_statements = self.parse_search_results(search_results)

        # Use Browserless to fetch additional market data
        market_data = BrowserTools.scrape_and_summarize_website("https://example.com/market-report")

        # Combine search results and market data into problem statements
        problems = self.combine_data(problem_statements, market_data)
        
        # Pass the problems to the Problem Reviewer
        self.manager.assign_problem_reviewer(problems)

    def parse_search_results(self, search_results):
        """
        Parse search results into a list of problem statements.
        
        :param search_results: The raw search results to be parsed.
        :return: A list of problem statements.
        """
        return [{"title": result} for result in search_results.split('\n') if result]

    def combine_data(self, problem_statements, market_data):
        """
        Combine problem statements and market data.
        
        :param problem_statements: A list of identified problem statements.
        :param market_data: Additional market data related to the problem statements.
        :return: A combined dictionary of problem statements and market data.
        """
        combined = {
            "problem_statements": problem_statements,
            "market_data": market_data
        }
        return combined

    def to_agent(self):
        """
        Convert the Problem Assessor instance to an Agent instance.
        
        :return: An Agent instance configured for problem assessment.
        """
        return Agent(
            role='Problem Assessor',
            goal='Identify and summarize the core problems that the idea aims to solve',
            backstory='An expert in analyzing market data and summarizing key problems.',
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
            ],
            verbose=True
        )
