import json
import os
import requests
from langchain.tools import tool
from unstructured.partition.html import partition_html
from crewai import Agent, Task

class BrowserTools:
    """
    Browser tools class for web scraping and summarization.
    """

    @tool("Scrape website content")
    def scrape_and_summarize_website(website):
        """
        Scrape and summarize content from a website.
        
        :param website: The URL of the website to scrape.
        :return: A summarized version of the website content.
        """
        url = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
        payload = json.dumps({"url": website})
        headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        
        # Check if response is successful
        if response.status_code != 200:
            raise Exception(f"Failed to scrape website: {response.status_code}")
        
        elements = partition_html(text=response.text)
        content = "\n\n".join([str(el) for el in elements])
        content_chunks = [content[i:i + 8000] for i in range(0, len(content), 8000)]
        summaries = []
        
        for chunk in content_chunks:
            agent = Agent(
                role='Principal Researcher',
                goal='Do amazing research and summaries based on the content you are working with',
                backstory="You're a Principal Researcher at a big company and you need to do research about a given topic.",
                allow_delegation=False)
            task = Task(
                agent=agent,
                description=f'Analyze and summarize the content below, make sure to include the most relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{chunk}'
            )
            summary = task.execute()
            summaries.append(summary)
        
        return "\n\n".join(summaries)

