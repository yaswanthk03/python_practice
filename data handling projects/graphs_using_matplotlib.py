"""
Sample data:
Date,City,Temperature,Condition
2025-06-11,Delhi,36.5,Clear
2025-06-12,Delhi,37.8,Sunny
2025-06-13,Delhi,38.0,Sunny
2025-06-14,Delhi,34.2,Rain
2025-06-15,Delhi,35.0,Clouds
2025-06-16,Delhi,33.4,Rain
2025-06-17,Delhi,34.7,Clear

Plot graphs from this data


"""
import os
import csv
from collections import Counter
import matplotlib.pyplot as plt

FILE_NAME = 'weather_log.csv'

def visualizer():

    temp = []
    dates = []
    conditions = Counter()
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for element in reader:
                temp.append(element['Temp'])
                dates.append(element['Date'])

                conditions[element['Condition']] += 1
        
    except Exception as e:
        print('Failed to load data from csv.', str(e))
        return
    if not dates:
        print("No data is available.")
        return
    
    plt.figure(figsize=(10,6))
    plt.plot(dates, temp, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Temp')
    
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(7,4))
    plt.bar(conditions.keys(), conditions.values(), color='green')
    plt.xlabel('Condition')
    plt.ylabel('No. of days')
    plt.tight_layout()
    plt.show()
    
visualizer()