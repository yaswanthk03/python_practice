"""
 Challenge: Scrape Books To Scrape (70 Books)

Goal:
- Visit https://books.toscrape.com/
- Scrape each book's:
  • Title 
  • Price 

You must:
- Crawl through multiple pages using the "next" button until you collect 70 books.
- Save the data to a JSON file: books_data.json
- Handle network errors gracefully.

Bonus:
- Track how many books scraped
- Print progress as you collect pages
"""

import json
import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com"
FILE_NAME = 'books_data.json'

def save_to_file(data):
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def urljoin(base_url, relative_url):
    if relative_url.startswith('http'):
        return relative_url
    if base_url.endswith('/'):
        base_url = base_url[:-1]
    if relative_url.startswith('/'):
        relative_url = relative_url[1:]
    
    if '.html' in base_url:
        base_url = ('/').join(base_url.split('/')[:-1])

    backslashes = relative_url.count('../')

    if backslashes:
        relative_url = relative_url.replace('../', '', backslashes)
        base_url = ('/').join(base_url.split('/')[:-(backslashes)])

    return f"{base_url}/{relative_url}"

def scrape_page(url) -> BeautifulSoup:
    
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

        soup = BeautifulSoup(request.text, 'html.parser')
        
    except requests.RequestException as e:
        raise RuntimeError(f"Network error: {e}")
    
    return soup

def extract_book_details(book_url):
    try:
        page = scrape_page(book_url)
        title = page.select(".product_main > h1")[0].text
        price = page.select(".product_main > .price_color")[0].text

        price = price.encode('latin-1').decode('utf-8')
        
        description_header_tag = page.find('div', id = 'product_description')

        description = description_header_tag.find_next('p').text
    except Exception as e:
        print("Book extraction failed.", str(e))
        raise Exception(e)
    
    book_details = {
        'Title': title,
        'Price': price,
        'Description': description
    }

    return book_details

def get_books(page_url, books_needed: int, book_details):

    try:
        page = scrape_page(page_url)
        curr_page_books_list = page.select('h3 > a')

    except Exception as e:
        print(f"Failed to extract page {page_url}.\n", str(e))
        return False
    
    

    for book in curr_page_books_list:
        
        if not books_needed:
            print(f'All the books are processed.')
            return True

        book_path = book.get("href", "").strip()
        book_title = book.text

        
        
        book_link = urljoin(page_url, book_path)
        
        try:
            book = extract_book_details(book_link)
            book_details.append(book)
            books_needed -= 1
            print(f"{book_title:<20} added to the data. ✅")
        except Exception as e:
            print(f"Failed to extract {book_title:<20} details. ❌", str(e))
            
    next_link_path = page.select_one(".next > a").get('href', "").split('/')

    if not next:
        print("No next page.")
        return False


    next_link = urljoin(page_url, '/'.join(next_link_path))
    return get_books(next_link, books_needed, book_details)

def main():

    data = []    

    try:
        get_books(URL, 2, data)
    except Exception as e:
        print("❌Extraction failed.❌", e)

    try:
        save_to_file(data)
    except Exception as e:
        print("❌Failed to save data.❌")
        return

    print(f'✅Saved {len(data)} books details.✅')

    return

if __name__ == '__main__':
    main()
    