"""
 Challenge: Store & Search Crypto Prices in SQLite

Goal:
- Save hourly top 10 crypto prices into a local SQLite database
- Each record should include timestamp, coin ID, and price
- Allow the user to search for a coin by name and return the latest price

Teaches: SQLite handling in Python, data storage, search queries, API + DB integration
"""

"""
depends on:
 - Day 7 of web scraping

Fetch crypto data every hour automatically

"""
import sqlite3
import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from matplotlib import pyplot as plt
import schedule
import time

load_dotenv()

API_URL = 'https://api.coingecko.com/api/v3/coins/markets'
API_KEY = os.getenv("COINGEKO_API_KEY")
FILE_NAME = 'crypto.csv'
DATABASE_NAME = 'cryptoDB'

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

def database_initiation():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS crypto_prices (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   timestamp TEXT,
                   name TEXT,
                   price REAL
                   )
''')
    conn.close()
    
def store_data(data):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect(DATABASE_NAME)
    cur = conn.cursor()
    
    for crypto in data:
        cur.execute('''
            INSERT INTO crypto_prices (timestamp, name, price)
                    VALUES (?, ?, ?)
                    
''', (timestamp, crypto['id'], crypto['current_price']))
        conn.commit()
    conn.close()

def search_db(coin_name):
    conn = sqlite3.connect(DATABASE_NAME)
    cur = conn.cursor()
    
    res = cur.execute('''
        SELECT timestamp, price
            FROM crypto_prices
            WHERE name = ?
            ORDER BY crypto_prices.id
''', (coin_name, ))
    
    conn.commit()
    
    times = []
    prices = []

    for tuple in res:
        times.append(tuple[0])
        prices.append(tuple[1])
    
    plt.plot(times, prices)
    plt.title(f'{coin_name} price chart')
    plt.xlabel('Date Time')
    plt.ylabel('Prices')
    plt.show()

    conn.close()


def main():
    database_initiation()
    data = fetch_crypto()
    if data: store_data(data)
    
    name = input("Coin name to search: ")
    if name: search_db(name)

# def job():
#     data = fetch_crypto()
#     if data: store_data(data)

if __name__ == '__main__':
    main()
    # schedule.every().hour.at(':00').do(job)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)