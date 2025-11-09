"""
 Challenge: Hacker News Top Posts Scraper

Build a Python script that:
1. Fetches the HN homepage (news.ycombinator.com).
2. Extracts the top 20 post titles and URLs.
3. Saves the results into a CSV file (`hn_top20.csv`) with columns:
   - Title
   - URL
4. Handles network errors and uses a clean CSV structure.
"""
# From HN homepage
# <span class="titleline">
#     <a href="https://github.com/aristocratos/btop">Btop: A better modern alternative of htop with a gamified interface</a>
#     <span class="sitebit comhead"> (<a href="from?site=github.com/aristocratos">
#         <span class="sitestr">github.com/aristocratos</span></a>)
#     </span>
# </span>

import csv
import requests
from bs4 import BeautifulSoup

FILE_NAME = 'hn_top20.csv'
URL = 'https://news.ycombinator.com/'

def save_to_file(data):
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Title', 'URL'])
        writer.writeheader()
        for item in data:
            writer.writerow(item)
        
        print("Successfully saved!")

def fetch_titles(url):

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
        print("Error ", str(e))
        return 
    
    try:
        soup = BeautifulSoup(request.text, 'html.parser')

        # spans = soup.find_all('span', class_='titleline', limit=20)

        posts = soup.select('span.titleline > a', limit=20)
        
        title_list = []

        # for span in spans:
        #     tag = span.find_all('a', recursive=False, limit=1)[0]
        #     title = tag.get_text(strip=True)
        #     link = tag.get('href', '')
        #     title_list.append({'Title': title, 'URL': link})

        for post in posts:
            title = post.get_text(strip=True)
            link = post.get('href', '').strip()
            title_list.append({'Title': title, 'URL': link})
        
        save_to_file(title_list)
        print('Data saved successfully!')
    except Exception as e:
        print("Error while parsing: ", str(e))

fetch_titles(URL)