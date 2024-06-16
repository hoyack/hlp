import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.utils.exa_util import ExaUtil

def main():
    exa_util = ExaUtil()

    # Test the search function
    search_query = "Top AI Companies"
    print(f"Search results for query '{search_query}':")
    try:
        search_results = exa_util.search(search_query)
        print(search_results)
    except Exception as e:
        print(f"Error in search function: {e}")

    # Test the find similar function
    find_similar_url = "hinge.co"
    print(f"\nFind similar results for URL '{find_similar_url}':")
    try:
        find_similar_results = exa_util.find_similar(find_similar_url)
        print(find_similar_results)
    except Exception as e:
        print(f"Error in find similar function: {e}")

    # Test the get contents function
    get_contents_ids = ["https://www.visitsanantonio.com/blog/post/discover-san-antonio-breweries-and-distilleries/"]
    print(f"\nGet contents results for URL '{get_contents_ids[0]}':")
    try:
        contents_results = exa_util.get_contents(get_contents_ids)
        print(contents_results)
    except Exception as e:
        print(f"Error in get contents function: {e}")

if __name__ == "__main__":
    main()
