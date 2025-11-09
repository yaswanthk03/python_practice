"""
 Challenge: Download Cover Images of First 10 Books

Goal:
- Visit https://books.toscrape.com/
- Scrape the first 10 books listed on the homepage
- For each book, extract:
  • Title
  • Image URL

Then:
- Download each image
- Save it to a local `images/` folder with the filename as the book title (sanitized)

Example:
 Title: "A Light in the Attic"
 Saved as: images/A_Light_in_the_Attic.jpg

Bonus:
- Handle invalid filename characters
- Show download progress
"""
import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import re

URL = 'https://books.toscrape.com/'
DIRECTORY = 'images'

def sanitize_filename(title):
    return re.sub(r'[^\w\-_. ]', '', title).replace(' ', '_')

def download_img(img_url, filepath):
    try:
        request = requests.get(img_url, stream=True, timeout=10)
        request.raise_for_status()

        with open(filepath, 'wb') as f:
            for chunk in request.iter_content(1024 * 8):
                f.write(chunk)
    except Exception as e:
        print('error', str(e))
        raise Exception
    
    return

def scrape_images(url):
    try:
        request = requests.get(url, timeout=10)
        request.raise_for_status()

        soup = BeautifulSoup(request.text, 'html.parser')

        articles = soup.find_all('article', class_ = {'product_pod'})[:10]

        for article in articles:
            img_relative_link = article.div.a.img['src'].strip()
            title = article.h3.a['title'].strip()
            
            title = sanitize_filename(title) + '.jpg'

            path = os.path.join(DIRECTORY, title)
            img_link = urljoin(url, img_relative_link)
            
            download_img(img_link, path)
            print(f'Image downloaded successfully!')
    except Exception as e:
        print("Failed downloading -", str(e))
    
def main():
    if not os.path.exists(DIRECTORY):
        os.mkdir('images')
    scrape_images(URL)

if __name__ == '__main__':
    main()