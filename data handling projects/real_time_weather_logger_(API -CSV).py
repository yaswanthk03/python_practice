"""
 Challenge: Real-Time Weather Logger (API + CSV)

Build a Python CLI tool that fetches real-time weather data for a given city and logs it to a CSV file for daily tracking.

Your program should:
1. Ask the user for a city name.
2. Fetch weather data using the OpenWeatherMap API.
3. Store the following in a CSV file (`weather_log.csv`):
   - Date (auto-filled as today's date)
   - City
   - Temperature (in °C)
   - Weather condition (e.g., Clear, Rain)
4. Prevent duplicate entries for the same city on the same day.
5. Allow users to:
   - Add new weather log
   - View all logs
   - Show average, highest, lowest temperatures, and most frequent condition

Bonus:
- Format the output like a table
- Handle API failures and invalid city names gracefully
"""

import csv
import os
from datetime import datetime
import requests

FILE_NAME = 'weather_log.csv'

if not os.path.exists(FILE_NAME):
     with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
          writer = csv.writer(f)
          writer.writerow(["Date", "City", "Temp", "Condition"])

def load_data():
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def get_weather(data):
    city = input("Enter city name: ")
    if not city:
        print("City can not be empty.")
        return
    
    date = datetime.now().strftime("%Y-%m-%d")

    for entry in data:
        if entry['Date'] == date and entry['City'].lower() == city.lower():
            print("Weather data already exists for this city on the same day.")
            return
    
    try:
        response = requests.get(f'https://wttr.in/{city.replace(" ", "+")}?m&format=%C+%f')
        response.raise_for_status()  # Raise an error for HTTP errors
    except:
        print("Failed to fetch weather data. Please check the city name or your internet connection.")
        return
    condition, temp = response.text.rsplit(' ', 1)

    with open(FILE_NAME, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([date, city, temp, condition])
    print(f"Weather data for {city} on {date} logged successfully.")
    data.append({"Date": date, "City": city, "Temp": temp, "Condition": condition})

def view_logs(data):
    if not data:
        print("No weather logs available.")
        return
    print(f"{'Date':<12} {'City':<20} {'Temp (°C)':<5} {'Condition':<15}")
    print("-" * 60)
    for entry in data:
        print(f"{entry['Date']:<12} {entry['City']:<20} {entry['Temp']:<5} {entry['Condition']:<15}")
        print("-" * 60)

def show_statistics(data):
    if not data:
        print("No weather data available for statistics.")
        return
    temps = [float(entry['Temp'].replace('°C', '').strip()) for entry in data]

    avg_temp = sum(temps) / len(temps)
    max_temp = max(temps)
    min_temp = min(temps)

    conditions = {}
    for entry in data:
        cond = entry['Condition']
        conditions[cond] = conditions.get(cond, 0) + 1
    
    most_frequent_condition = max(conditions, key=conditions.get)
    print(f"Average Temperature: {avg_temp:.2f}°C")
    print(f"Highest Temperature: {max_temp:.2f}°C")
    print(f"Lowest Temperature: {min_temp:.2f}°C")
    print(f"Most Frequent Condition: {most_frequent_condition}")

def main():
    data = load_data()
    while True:
        print("\nWeather Logger Menu:")
        print("1. Add new weather log")
        print("2. View all logs")
        print("3. Show statistics")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            get_weather(data)
        elif choice == '2':
            view_logs(data)
        elif choice == '3':
            show_statistics(data)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            
if __name__ == "__main__":
    main()