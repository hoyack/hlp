from exa_py import Exa
import os
from dotenv import load_dotenv


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


def ExaSearch_Tool(query: str) -> str:
    exa_util = ExaUtil()
    try:
        results = exa_util.search(query)
        return results
    except Exception as e:
        return f"Error performing search: {e}"


def ExaFindSimilar_Tool(url: str) -> str:
    exa_util = ExaUtil()
    try:
        results = exa_util.find_similar(url)
        return results
    except Exception as e:
        return f"Error finding similar content: {e}"


def ExaGetContents_Tool(ids: str) -> str:
    exa_util = ExaUtil()
    try:
        results = exa_util.get_contents(ids)
        return results
    except Exception as e:
        return f"Error getting contents: {e}"
