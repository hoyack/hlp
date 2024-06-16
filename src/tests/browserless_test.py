# src/tests/browserless_test.py

import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.utils.browserless_util import BrowserlessUtil

def main():
    test_url = "https://www.visitsanantonio.com/blog/post/discover-san-antonio-breweries-and-distilleries/"
    browserless_util = BrowserlessUtil()
    try:
        cleaned_content = browserless_util.fetch_and_clean_content(test_url)
        print("Cleaned Content:\n", cleaned_content)
    except Exception as e:
        print(f"Error fetching and cleaning content: {e}")

if __name__ == "__main__":
    main()
