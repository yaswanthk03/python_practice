"""
 Challenge: Scrape Wikipedia h2 Headers

Use the `requests` and `BeautifulSoup` libraries to fetch the Wikipedia page on Python (programming language).

Your task is to:
1. Download the HTML of the page.
2. Parse all `<h2>` section headers.
3. Store the clean header titles in a list.
4. Print the total count and display the first 10 section titles.

Bonus:
- Remove any trailing "[edit]" from the headers.
- Handle network errors gracefully.
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

def get_h2_headers(url):
    
    # Headers to prevent server from rejection bot requests.
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/58.0.3029.110 Safari/537.3"
        )
    }

    try:
        request = requests.get(url, headers=headers, timeout=10)
        request.raise_for_status()
    except requests.RequestException as e:
        print("Error: ", str(e))
        return []
    
    soup = BeautifulSoup(request.text, 'html.parser')
    h2_tags = soup.find_all('h2')

    return h2_tags

def main():
    tags = get_h2_headers(URL)

    print(f'There are {len(tags)} h2 header.\nThe first 10 are: ')
    for tag in tags[:10]:
        print(tag.get_text(strip=True))

if __name__ == '__main__':
    main()