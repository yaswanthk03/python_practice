"""
 Challenge: Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

Example:
If the user inputs:
  Name: Priya
  Age: 22
  City: Jaipur
  Profession: Software Developer
  Hobby: playing guitar

Your script might output:
  "Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!"

Bonus:
- Add the current date to the end of the paragraph like: "Logged on: 2025-06-14"
- Wrap the printed message with a decorative border of stars (*)
"""

import datetime
# Collect user information

def validate_age(age_str):
    try:
        age = int(age_str)
        if age <= 0:
            raise ValueError
        return age
    except ValueError:
        print("Please enter a valid positive integer for age.")
        return None

name = input("Enter your name: ").strip()

while True:
    age = input("Enter your age: ").strip()
    age = validate_age(age)
    if age is not None:
        break

city = input("Enter your city: ").strip()
profession = input("Enter your profession: ").strip()
hobby = input("Enter your favorite hobby: ").strip()

date = datetime.date.today()

print("\n" + "*" * 100)
print(f"Hello! My name is {name}. I'm {age} years old and live in {city}. I work as a {profession} and I absolutely enjoy {hobby} in my free time. Nice to meet you!")
print(f"Logged on: {date}")

print('\n' + '*' * 100)