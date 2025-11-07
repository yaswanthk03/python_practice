"""
 Challenge: Offline Notes Locker

Create a terminal-based app that allows users to save, view, and search personal notes securely in an encrypted file.

Your program should:
1. Let users add notes with title and content.
2. Automatically encrypt each note using Fernet (AES under the hood).
3. Store all encrypted notes in a single `.vault` file (JSON format).
4. Allow listing of titles and viewing/decrypting selected notes.
5. Support searching by title or keyword.

Bonus:
- Add timestamps to notes.
- Use a master password to unlock vault (optional).
"""

import os
import json
from datetime import datetime
from cryptography.fernet import Fernet
import hashlib
import getpass  # For secure password input

VAULT_FILE = 'vault.json'
KEY_FILE = 'secret.key'
PASS_FILE = 'master.hash'

def set_master_password():
    while True:
        password = getpass.getpass("Set a password: ")
        confirm = getpass.getpass("Confirm password: ")
        if password == confirm:

            password_hash = hashlib.sha256(password.encode()).hexdigest()
            with open(PASS_FILE, 'w') as f:
                f.write(password_hash)
            return True
        print("Password does not match.")

def verify_password():
    if not os.path.exists(PASS_FILE):
        print("First time setup - create a master password.")
        return set_master_password()
    password = getpass.getpass("Enter master key: ")

    stored_hash = open(PASS_FILE, 'r').read().strip()
    current_hash = hashlib.sha256(password.encode()).hexdigest()

    return current_hash == stored_hash

def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'rb') as file:
            key = file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as file:
            file.write(key)
    return Fernet(key)

def load_vault():
    if not os.path.exists(VAULT_FILE):
        return []
    with open(VAULT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def view_notes(data):
    for i, note in enumerate(data, 1):
        print(f"{i}. {note['title']} {note['datetime']}.")

def add_notes():

    title = input("Enter Title: ").strip()
    content = input("Enter content: ").strip()
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not title or not content:
        print("Title or Content can't be empty.")
        return
    
    data = load_vault()
    fernet = load_key()

    encrypted_content = fernet.encrypt(content.encode()).decode()
    
    data.append({
        'title': title,
        'content': encrypted_content,
        'datetime': time
    })

    with open(VAULT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ Successfully added {title} at {time}.")

def get_notes():

    data = load_vault()

    if not data:
        print("No notes found. Please add some notes first.")
        return

    view_notes(data)
    fernet = load_key()

    try:
        id = int(input("Enter the id of the notes to view (select from above options).: ")) - 1
        if not 0 <= id <= len(data):
            print("Enter an id in the range.")
        
        content = fernet.decrypt(data[id]['content'].encode()).decode()

        print(f"\n Title:- {data[id]['title']}    {data[id]['datetime']}\n Content: {content}.")
    except:
        print("Enter a valid number.")

def search_notes():
    key = input("Enter a key string to search: ").strip().lower()

    if not key:
        print("Key can't be empty")
        return
    
    notes = load_vault()

    found = False
    for note in enumerate(notes, 1):
        if key in note['title']:
            print(f"{note['title']} {note['datetime']}.")
            found = True

    if not found:
        print("No notes found with the given key.")

def main():
    if not verify_password():
        print("Incorrect password! Try again.")
        return 

    while True:
        print("\n1. Add Note\n2. View Note\n3. Search Note\n4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_notes()
        elif choice == '2':
            get_notes()
        elif choice == '3':
            search_notes()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()