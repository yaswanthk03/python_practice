"""
depends on:
 - Day 7 of web scraping

Fetch crypto data every hour automatically

"""

import os
import requests
from datetime import datetime
from dotenv import load_dotenv
import csv
import schedule
import time

load_dotenv()

API_URL = 'https://api.coingecko.com/api/v3/coins/markets'
API_KEY = os.getenv("COINGEKO_API_KEY")
FILE_NAME = 'crypto.csv'

def save_file(data):
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(FILE_NAME, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for coin in data:
            writer.writerow([coin['id'], coin['current_price'], time])
        print("File saved successfully. ✅")

def fetch_crypto():
    params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 20
    }
    headers = {"x-cg-demo-api-key": API_KEY}

    try:
        request = requests.get(API_URL, headers=headers, params=params, timeout=10)
        request.raise_for_status()
        return request.json()
    except requests.RequestException as e:
        print(f"Request failed - {e}")
    
    return []

def main():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w') as f:
            csv.writer(f).writerow(['Crypto', 'Price', 'Time'])

def job():
    data = fetch_crypto()
    if data: save_file(data)

if __name__ == '__main__':
    main()
    schedule.every().hour.at(':00').do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)