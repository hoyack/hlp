from exa_py import Exa
import os
from dotenv import load_dotenv
from crewai_tools import BaseTool

# Load environment variables from .env file
load_dotenv()

class ExaUtil:
    def __init__(self):
        self.api_key = os.getenv("EXA_API_KEY")
        if not self.api_key:
            raise ValueError("Error: EXA_API_KEY not found in environment variables.")
        self.exa = Exa(api_key=self.api_key)

    def search(self, query, num_results=1, text=True):
        return self.exa.search_and_contents(
            query,
            type="neural",
            use_autoprompt=True,
            num_results=num_results,
            text=text
        )

    def find_similar(self, url, num_results=3, text=True, exclude_domains=None):
        exclude_domains = exclude_domains if exclude_domains else [url]
        return self.exa.find_similar_and_contents(
            url,
            num_results=num_results,
            text=text,
            exclude_domains=exclude_domains
        )

    def get_contents(self, ids, text=True):
        if not isinstance(ids, list):
            ids = [ids]
        return self.exa.get_contents(ids, text=text)



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
