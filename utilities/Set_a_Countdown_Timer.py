"""
Challenge: Set a Countdown Timer

Create a Python script that allows the user to set a timer in seconds. The script should:

1. Ask the user for the number of seconds to set the timer.
2. Show a live countdown in the terminal.
3. Notify the user when the timer ends with a final message and sound (if possible).

Bonus:
- Format the remaining time as MM:SS
- Use a beep sound (`\a`) at the end if the terminal supports it
- Prevent negative or non-integer inputs
"""

import time

def main():
    
    while True:
        try: 
            timer_in_seconds = int(input("⏰ Enter countdown timer in seconds: ").strip())
            if timer_in_seconds <= 0:
                print("Please enter a valid time greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a whole number.")

    print("----Timer started----")

    for remaining in range(timer_in_seconds, -1, -1):
        min, sec = divmod(remaining, 60)
        time_format = f"{min:02} : {sec:02} s"
        print(f'Time remaining ==> {time_format}', end='\r')
        time.sleep(1)
    else:
        print("\n----Time is up----")
main()