# src/utils/browserless_util.py

import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


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


def Browserless_Tool(url: str) -> str:
    browserless_util = BrowserlessUtil()
    try:
        cleaned_content = browserless_util.fetch_and_clean_content(url)
        return cleaned_content
    except Exception as e:
        return f"Error fetching and cleaning content: {e}"
