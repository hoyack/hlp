# src/utils/duckduckgo_util.py

from langchain.tools import DuckDuckGoSearchResults
from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun
import re

class DuckDuckGoUtil:
    def __init__(self):
        self.search_tool = DuckDuckGoSearchResults()

    def search(self, query, num_results=10):
        return self.search_tool.run(query, num_results=num_results)

    def parse_search_results(self, results):
        parsed_results = []
        pattern = re.compile(r"\[snippet: (.*?), title: (.*?), link: (.*?)\]")
        matches = pattern.findall(results)

        for match in matches:
            parsed_results.append({
                "snippet": match[0],
                "title": match[1],
                "link": match[2]
            })

        return parsed_results

    def format_search_results(self, parsed_results):
        formatted_results = ""
        for result in parsed_results:
            formatted_results += f"Title: {result['title']}\n"
            formatted_results += f"Snippet: {result['snippet']}\n"
            formatted_results += f"Link: {result['link']}\n\n"

        return formatted_results


class DuckDuckGoCommunityUtil:
    def __init__(self):
        self.search_tool = DuckDuckGoSearchRun()

    def search(self, query, num_results=10):
        # DuckDuckGoSearchRun does not support a 'num_results' parameter in its 'run' method.
        return self.search_tool.run(query)

    def format_raw_output(self, raw_output):
        # Insert a new line after each occurrence of "..."
        formatted_output = raw_output.replace("...", "...\n")
        return formatted_output


class DuckDuckGoNewsUtil:
    def __init__(self):
        self.search_tool = DuckDuckGoSearchResults(backend="news")

    def search(self, query, num_results=10):
        return self.search_tool.run(query, num_results=num_results)

    def parse_search_results(self, results):
        parsed_results = []
        pattern = re.compile(r"\[snippet: (.*?), title: (.*?), link: (.*?), date: (.*?), source: (.*?)\]")
        matches = pattern.findall(results)

        for match in matches:
            parsed_results.append({
                "snippet": match[0],
                "title": match[1],
                "link": match[2],
                "date": match[3],
                "source": match[4]
            })

        return parsed_results

    def format_search_results(self, parsed_results):
        formatted_results = ""
        for result in parsed_results:
            formatted_results += f"Title: {result['title']}\n"
            formatted_results += f"Snippet: {result['snippet']}\n"
            formatted_results += f"Link: {result['link']}\n"
            formatted_results += f"Date: {result['date']}\n"
            formatted_results += f"Source: {result['source']}\n\n"

        return formatted_results
