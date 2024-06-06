import json
import os
import requests
from langchain.tools import tool

class SearchTools:
    """
    Search tools class for performing internet searches.
    """

    @tool("Search the internet")
    def search_internet(query):
        """
        Perform an internet search and return relevant results.
        
        :param query: The search query to perform.
        :return: A string containing the top search results.
        """
        top_result_to_return = 4
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        results = response.json().get('organic', [])
        string = []
        for result in results[:top_result_to_return]:
            try:
                string.append('\n'.join([
                    f"Title: {result['title']}", f"Link: {result['link']}",
                    f"Snippet: {result['snippet']}", "\n-----------------"
                ]))
            except KeyError:
                continue

        return '\n'.join(string)

    @tool("Search news on the internet")
    def search_news(query):
        """
        Perform a news search and return relevant results.
        
        :param query: The news search query to perform.
        :return: A string containing the top news results.
        """
        top_result_to_return = 4
        url = "https://google.serper.dev/news"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        results = response.json().get('news', [])
        string = []
        for result in results[:top_result_to_return]:
            try:
                string.append('\n'.join([
                    f"Title: {result['title']}", f"Link: {result['link']}",
                    f"Snippet: {result['snippet']}", "\n-----------------"
                ]))
            except KeyError:
                continue

        return '\n'.join(string)
