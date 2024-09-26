# src/utils/browserless_util.py

import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from crewai_tools import BaseTool


# Load environment variables from .env file
load_dotenv()

class BrowserlessUtil:
    def __init__(self):
        self.api_key = os.getenv("BROWSERLESS_API_KEY")
        if not self.api_key:
            raise ValueError("Error: BROWSERLESS_API_KEY not found in environment variables.")

    def fetch_url_content(self, url):
        with sync_playwright() as p:
            browser = p.firefox.connect(f'wss://chrome.browserless.io/playwright?token={self.api_key}')
            context = browser.new_context()
            page = context.new_page()
            page.goto(url, wait_until='domcontentloaded')
            content = page.content()
            context.close()
            return content

    def clean_html(self, html_content):
        soup = BeautifulSoup(html_content, 'lxml')
        for script in soup(["script", "style"]):
            script.decompose()
        cleaned_text = ' '.join(soup.stripped_strings)
        return cleaned_text

    def fetch_and_clean_content(self, url):
        raw_content = self.fetch_url_content(url)
        cleaned_content = self.clean_html(raw_content)
        return cleaned_content


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
