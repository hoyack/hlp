# src/utils/duckduckgo_util.py

from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun
import re
from crewai_tools import BaseTool


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


class DuckDuckGoSearchTool(BaseTool):
    name: str = "DuckDuckGoSearchTool"
    description: str = "A tool for performing web searches using DuckDuckGo."

    def _run(self, query: str) -> str:
        ddg_util = DuckDuckGoUtil()
        try:
            search_results = ddg_util.search(query)
            parsed_results = ddg_util.parse_search_results(search_results)
            formatted_results = ddg_util.format_search_results(parsed_results)
            return formatted_results
        except Exception as e:
            return f"Error performing search: {e}"

    def _arun(self, query: str):
        raise NotImplementedError("DuckDuckGoSearchTool does not support async")

    def _cache_key(self, *args, **kwargs) -> str:
        return f"{self.name}:{args[0]}"


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


class DuckDuckGoCommunitySearchTool(BaseTool):
    name: str = "DuckDuckGoCommunitySearchTool"
    description: str = "A tool for performing web searches using the DuckDuckGo Community."

    def _run(self, query: str) -> str:
        ddg_community_util = DuckDuckGoCommunityUtil()
        try:
            search_results = ddg_community_util.search(query)
            formatted_results = ddg_community_util.format_raw_output(search_results)
            return formatted_results
        except Exception as e:
            return f"Error performing search: {e}"

    def _arun(self, query: str):
        raise NotImplementedError("DuckDuckGoCommunitySearchTool does not support async")

    def _cache_key(self, *args, **kwargs) -> str:
        return f"{self.name}:{args[0]}"
    

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


class DuckDuckGoNewsSearchTool(BaseTool):
    name: str = "DuckDuckGoNewsSearchTool"
    description: str = "A tool for performing news searches using DuckDuckGo."

    def _run(self, query: str) -> str:
        ddg_news_util = DuckDuckGoNewsUtil()
        try:
            search_results = ddg_news_util.search(query)
            parsed_results = ddg_news_util.parse_search_results(search_results)
            formatted_results = ddg_news_util.format_search_results(parsed_results)
            return formatted_results
        except Exception as e:
            return f"Error performing search: {e}"

    def _arun(self, query: str):
        raise NotImplementedError("DuckDuckGoNewsSearchTool does not support async")

    def _cache_key(self, *args, **kwargs) -> str:
        return f"{self.name}:{args[0]}"
