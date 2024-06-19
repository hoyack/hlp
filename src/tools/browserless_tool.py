# tools/browserless_tool.py
from crewai_tools import BaseTool
from src.utils.browserless_util import BrowserlessUtil

class BrowserlessTool(BaseTool):
    name: str = "BrowserlessTool"
    description: str = "A tool for scraping websites using Browserless. It fetches and cleans the content of a webpage. It requires a input of a URL in a format like https://example.com."

    def _run(self, url: str) -> str:
        browserless_util = BrowserlessUtil()
        try:
            cleaned_content = browserless_util.fetch_and_clean_content(url)
            return cleaned_content
        except Exception as e:
            return f"Error fetching and cleaning content: {e}"

    def _arun(self, url: str):
        raise NotImplementedError("BrowserlessTool does not support async")

    def _cache_key(self, *args, **kwargs) -> str:
        return f"{self.name}:{args[0]}"
