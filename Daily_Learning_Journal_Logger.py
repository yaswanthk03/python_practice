"""
 Challenge: Daily Learning Journal Logger

Build a Python script that allows you to maintain a daily learning journal. Each entry will be saved into a `.txt` file along with a timestamp.

Your program should:
1. Ask the user what they learned today.
2. Add the entry to a file called `learning_journal.txt`.
3. Each entry should include the date and time it was written.
4. The journal should **append** new entries rather than overwrite.

Bonus:
- Add an optional rating (1-5) for how productive the day was.
- Show a confirmation message after saving the entry.
- Make sure the format is clean and easy to read when opening the file.

Example:
📅 2025-06-14 — 10:45 AM
Today I learned about how list comprehensions work in Python!
Productivity Rating: 4/5
"""

import datetime

now = datetime.datetime.now()
now.strfti

entry = f"📅 {datetime.datetime.now().strftime("%d-%m-%Y  %I:%M:%S %p")}\n"

entry += input("Type today's Journal: ").strip() + "\n"

prod_rating = input("Enter a productivity rating in the range of 1 to 5: ")

try:
    prod_rating = float(prod_rating)
    if prod_rating < 1 or prod_rating > 5:
        raise ValueError("wrong value range")
except:
    print("Missing valid rating")

if type(prod_rating) == float:
    entry += f"Productivity Rating: {prod_rating}/5\n"

entry += '"""\n\n'
try:
    with open('learning_journal.txt', "a", encoding="utf-8") as file:
        file.write(entry)
    print("Entry filed successfully.")
except Exception as e:
    print(f"Error filing the entry: {e}")

