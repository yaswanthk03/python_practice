"""
Challenge : JSON Flattener

{
  "user": {
    "id": 1,
    "name": "Riya",
    "email": "riya@example.com",
    "address": {
      "city": "Delhi",
      "pincode": 110001
    }
  },
  "roles": ["admin", "editor"],
  "is_active": true
}

Flatten this to:

{
  "user.id": 1,
  "user.name": "Riya",
  "user.email": "riya@example.com",
  "user.address.city": "Delhi",
  "user.address.pincode": 110001,
  "roles.0": "admin",
  "roles.1": "editor",
  "is_active": true
}


"""

import json
import os

INPUT_FILE = "nested_data.json"
OUTPUT_FILE = "flattened_data.json"

def flatten(data, res, parent_key='', sep='.'):

    if type(data) == dict:
        for key, value in data.items():
            flatten(value, res, f'{parent_key}{key}{sep}', sep)

    elif type(data) == list:
        for idx, value in enumerate(data):
            flatten(value, res, f'{parent_key}{idx}{sep}', sep)

    else:
        res[parent_key[:-1]] = data
        return 
    
    return

def main():
    if not os.path.exists(INPUT_FILE):
        print("No input file found.")
        return
    
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        sep = input("Enter separator (default is . ): ") or '.'
        flattened_data = {}
            
        flatten(data, flattened_data, sep=sep)
        
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(flattened_data, f, indent=2)
        print("File flattened successfully.👍")

    except Exception as e:
        print(f"Failed to flatten the json. Error: {str(e)}")
    
if __name__ == "__main__":
    main()