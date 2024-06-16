# src/tests/duckduckgo_test.py

import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.utils.duckduckgo_util import DuckDuckGoUtil, DuckDuckGoCommunityUtil, DuckDuckGoNewsUtil

def main():
    # Test the original DuckDuckGo search implementation
    ddg_util = DuckDuckGoUtil()

    search_query = "Best Vacation Spots"
    print(f"Search results for query '{search_query}' using DuckDuckGoUtil:")
    try:
        search_results = ddg_util.search(search_query)
        parsed_results = ddg_util.parse_search_results(search_results)
        formatted_results = ddg_util.format_search_results(parsed_results)
        print(formatted_results)
    except Exception as e:
        print(f"Error in search function using DuckDuckGoUtil: {e}")

    # Test the community DuckDuckGo search implementation
    ddg_community_util = DuckDuckGoCommunityUtil()

    print(f"Search results for query '{search_query}' using DuckDuckGoCommunityUtil (formatted):")
    try:
        search_results = ddg_community_util.search(search_query)
        formatted_results = ddg_community_util.format_raw_output(search_results)
        print(formatted_results)
    except Exception as e:
        print(f"Error in search function using DuckDuckGoCommunityUtil: {e}")

    # Test the news DuckDuckGo search implementation
    ddg_news_util = DuckDuckGoNewsUtil()

    print(f"Search results for query '{search_query}' using DuckDuckGoNewsUtil (formatted):")
    try:
        search_results = ddg_news_util.search(search_query)
        parsed_results = ddg_news_util.parse_search_results(search_results)
        formatted_results = ddg_news_util.format_search_results(parsed_results)
        print(formatted_results)
    except Exception as e:
        print(f"Error in search function using DuckDuckGoNewsUtil: {e}")

if __name__ == "__main__":
    main()
