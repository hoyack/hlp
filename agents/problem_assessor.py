from tools.browserless_tool import BrowserTools
from tools.serper_tool import SearchTools
from crewai import Agent

class ProblemAssessor:
    def __init__(self, manager):
        self.manager = manager

    def assess_problem(self, idea_summary):
        # Use Serper to perform search
        search_results = SearchTools.search_internet(f"pain points in {idea_summary}")
        problem_statements = self.parse_search_results(search_results)

        # Use Browserless to fetch additional market data
        market_data = BrowserTools.scrape_and_summarize_website("https://example.com/market-report")

        # Combine results into problem statements
        problems = self.combine_data(problem_statements, market_data)
        
        # Pass the problems to the Problem Reviewer
        self.manager.assign_problem_reviewer(problems)

    def parse_search_results(self, search_results):
        # Convert search results to a list of problem statements
        return [{"title": result} for result in search_results.split('\n') if result]

    def combine_data(self, problem_statements, market_data):
        # Process and combine data into problem statements
        combined = {
            "problem_statements": problem_statements,
            "market_data": market_data
        }
        return combined

    def to_agent(self):
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
