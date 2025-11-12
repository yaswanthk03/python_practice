"""
 Challenge: Real-Time System Resource Monitor

Goal:
- Monitor your system's CPU, RAM, and Disk usage
- Print updates every few seconds
- Warn user if CPU or RAM usage exceeds 80%
- Runs in terminal as a live dashboard

Teaches: psutil, formatting, real-time monitoring, conditional logic
Tools: psutil, time
"""

import os
import time
import psutil

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_stats():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    clear_screen()

    print("🔥" * 30)
    print(' ' * 10,"System stats:-")

    print(f'Cpu usage - {cpu}%')
    print(f'Ram usage {ram.percent}% ({round(ram.used / 1e9, 2)} GB used in {ram.total // 1e9} GB)')
    print(f'Disk usage {disk.percent}% ({round(disk.used / 1e9, 2)} GB used in {disk.total // 1e9} GB)')

if __name__ == '__main__':
    try:
        while True:
            show_stats()
            time.sleep(3)
    except KeyboardInterrupt:
        print("System monitoring stopped.✅")