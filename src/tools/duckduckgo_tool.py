# tools/duckduckgo_tool.py

from crewai_tools import BaseTool
from src.utils.duckduckgo_util import DuckDuckGoUtil, DuckDuckGoCommunityUtil, DuckDuckGoNewsUtil

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
