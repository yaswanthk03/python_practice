"""
 Challenge: Password Strength Checker & Suggestion Tool

Build a Python script that checks the strength of a password based on:
1. Length (at least 8 characters)
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one digit
5. At least one special character (e.g., @, #, $, etc.)

Your program should:
- Ask the user to input a password.
- Tell them what's missing if it's weak.
- If the password is strong, confirm it.
- Suggest a strong random password if the input is weak.

Bonus:
- Hide password input using `getpass` (no echo on screen).
"""

import getpass
import string
import random

def password_strength_test(password:str) -> list[str]:

    fails = []
    if len(password) < 8:
        fails.append("Password should contain minimum 8 characters")
    if not any(x.isupper() for x in password):
        fails.append("password should contain at least 1 Upper case letter.")
    if not any(x.islower() for x in password):
        fails.append("password should contain at least 1 Lower case letter.")
    if not any(x.isdigit() for x in password):
        fails.append("password should contain at least 1 Digit.")
    if not any(x in string.punctuation for x in password):
        fails.append("password should contain at least 1 Special character.")
    
    return fails

def strong_password_generator(length=12):
    
    chars = string.ascii_letters + string.digits + string.punctuation
    
    password = list(random.choice(chars) for _ in range(8))

    password.insert(int(random.random() * 8), random.choice(string.punctuation))
    password.insert(int(random.random() * 9), random.choice(string.digits))
    password.insert(int(random.random() * 10), random.choice(string.ascii_uppercase))
    password.insert(int(random.random() * 11), random.choice(string.ascii_lowercase))

    return "".join(password)


def main():
    password = getpass.getpass("Enter password: ")
    fails = password_strength_test(password)
    if not fails:
        print("Your password is strong.")
    else:
        for fail in fails:
            print(fail)
        print("Suggesting a password:", strong_password_generator())

main()