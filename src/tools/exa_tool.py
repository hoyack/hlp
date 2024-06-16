# tools/exa_tool.py

from crewai_tools import BaseTool
from utils.exa_util import ExaUtil

class ExaSearchTool(BaseTool):
    name: str = "ExaSearchTool"
    description: str = "A tool for performing searches using the EXA service. It takes a search inpute like: Top AI Companies"

    def _run(self, query: str) -> str:
        exa_util = ExaUtil()
        try:
            results = exa_util.search(query)
            return results
        except Exception as e:
            return f"Error performing search: {e}"

    def _arun(self, query: str):
        raise NotImplementedError("ExaSearchTool does not support async")

    def _cache_key(self, *args, **kwargs) -> str:
        return f"{self.name}:{args[0]}"

class ExaFindSimilarTool(BaseTool):
    name: str = "ExaFindSimilarTool"
    description: str = "A tool for finding similar content using the EXA service."

    def _run(self, url: str) -> str:
        exa_util = ExaUtil()
        try:
            results = exa_util.find_similar(url)
            return results
        except Exception as e:
            return f"Error finding similar content: {e}"

    def _arun(self, url: str):
        raise NotImplementedError("ExaFindSimilarTool does not support async")

    def _cache_key(self, *args, **kwargs) -> str:
        return f"{self.name}:{args[0]}"

class ExaGetContentsTool(BaseTool):
    name: str = "ExaGetContentsTool"
    description: str = "A tool for getting contents using the EXA service. It takes a URL as the input."

    def _run(self, ids: str) -> str:
        exa_util = ExaUtil()
        try:
            results = exa_util.get_contents(ids)
            return results
        except Exception as e:
            return f"Error getting contents: {e}"

    def _arun(self, ids: str):
        raise NotImplementedError("ExaGetContentsTool does not support async")

    def _cache_key(self, *args, **kwargs) -> str:
        return f"{self.name}:{args[0]}"
