"""
 Challenge: Crypto Price Tracker with Graphs

Goal:
- Fetch live prices of the top 10 cryptocurrencies using CoinGecko's free public API
- Store prices in a CSV file with timestamp
- Generate a line graph for a selected coin over time (price vs. time)
- Repeatable — user can run this multiple times to log data over time

JSON handling, API usage, CSV storage, matplotlib graphing
"""

import os
import requests
from datetime import datetime
from matplotlib import pyplot as plt
from dotenv import load_dotenv
import csv

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

def draw_graph(coin_name: str):

    prices, time_stamps = [], []
    with open(FILE_NAME, 'r') as f:
        reader = csv.DictReader(f)

        for crypto in reader:
            if crypto['Crypto'] == coin_name:
                prices.append(crypto['Price'])
                time_stamps.append(crypto['Time'])

    if not prices:
        print("No data to show.")
        return
    
    # plt.figure(figsize=(50, 50))
    plt.plot( time_stamps, prices)
    plt.title(f"{coin_name} price history.")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.show()

def main():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w') as f:
            csv.writer(f).writerow(['Crypto', 'Price', 'Time'])

    data = fetch_crypto()
    save_file(data)

    coin_name = input("Enter a coin name to see price chart: ").strip()
    if coin_name:
        draw_graph(coin_name)

if __name__ == '__main__':
    main()