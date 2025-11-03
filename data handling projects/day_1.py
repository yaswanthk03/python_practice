"""
 Challenge: CLI Contact Book (CSV-Powered)

Create a terminal-based contact book tool that stores and manages contacts using a CSV file.

Your program should:
1. Ask the user to choose one of the following options:
   - Add a new contact
   - View all contacts
   - Search for a contact by name
   - Exit
2. Store contacts in a file called `contacts.csv` with columns:
   - Name
   - Phone
   - Email
3. If the file doesn't exist, create it automatically.
4. Keep the interface clean and clear.

Example:
Add Contact
View All Contacts
Search Contact
Exit

Bonus:
- Format the contact list in a table-like view
- Allow partial match search
- Prevent duplicate names from being added
"""
import csv
import os

FILE_NAME = 'contacts.csv'

if not os.path.exists(FILE_NAME):
     
     with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
          writer = csv.writer(f)
          writer.writerow(["Name", "Phone", "Email"])


def add_contact():
      name = input("Name: ").strip()
      while not name:
         name = input("Name must not be empty").strip()
            
      phone = input("Phone number: ").strip()
      email = input("Email: ").strip()

      #check for duplicate names

      with open(FILE_NAME, 'r', encoding="utf-8") as f:
           reader = csv.DictReader(f)
           for contact in reader:
                if contact["Name"] == name:
                     print("Contact already exists.")
                     return
      
      with open(FILE_NAME, 'a', newline="", encoding='utf-8') as f:
           writer = csv.writer(f)
           writer.writerow([name, phone, email])
           print("Contact added successfully.")

def view_contacts():
     with open(FILE_NAME, 'r', encoding="utf-8") as f:
           reader = csv.reader(f)
           headers = next(reader, None)
           contacts = list(reader)
           if not contacts:
                print("There are no contacts.")
                return
           
           print("{:03} {:<20} {:<15} {:<30}".format("No.", *headers))
           print("-" * 60)
           for idx, contact in enumerate(contacts, start=1):
                name, phone, email = (contact + [""] * 3)[:3]
                print(f"{idx:<4} {name:<20} {phone:<15} {email:<30}")

def search_contact():
     name = input("Name: ").strip()
     while not name:
           name = input("Name must not be empty").strip().lower()

     with open(FILE_NAME, 'r', encoding="utf-8") as f:
           reader = csv.DictReader(f)
           matches_found = False
           for contact in reader:
                if name in contact["Name"].lower():
                     print(f"{contact["Name"]:<15} {contact["Phone"]:<12} {contact["Email"]:<30}")
                     matches_found = True
           if not matches_found:
                print("No matches found")

def edit_contact():
     name = input("Name: ").strip()
     while not name:
           name = input("Name must not be empty").strip().lower()
     new_phone = input("Phone number: ").strip()
     new_email = input("Email: ").strip()
     
     with open(FILE_NAME, 'r', encoding="utf-8") as f:
           reader = csv.reader(f)
           contacts = list(reader)
     
     for contact in contacts[1:]:
          if contact[0] == name:
               contact[1] = new_phone
               contact[2] = new_email
               break
     else:
           print("No match found for the name.")
           return
     
     with open(FILE_NAME, 'w', newline="", encoding='utf-8') as f:
          writer = csv.writer(f)
          writer.writerows(contacts)
          print("Contact edited successfully.")
           

def delete_contact():
     name = input("Name: ").strip()
     name_found, new_contacts = False, []
     while not name:
           name = input("Name must not be empty").strip().lower()
     
     with open(FILE_NAME, 'r', encoding="utf-8") as f:
           contacts = csv.DictReader(f)
           for contact in contacts:
               if contact['Name'] != name:
                    new_contacts.append(contact)
               else:
                    name_found = True
     if not name_found:
           print("No match found for the name.")
           return
     fields = list(new_contacts[0].keys())
     with open(FILE_NAME, 'w', newline="", encoding='utf-8') as f:
          writer = csv.DictWriter(f, fieldnames=fields)
          writer.writeheader()

          writer.writerows(new_contacts)
          print("Contact deleted successfully.")
           
def main():
     print("Welcome to Contact Book.")
     while True:
          print("Options: ")
          print("1. Add a new contact \n2. View all contacts \n3. Search for a contact by name")
          print("4. Edit a contact  by name \n5. Delete a contact  by name \n6. Exit")

          option = input("Print an option from (1 - 6): ")
          
          match option:
               case '1':
                    add_contact()
               case '2':
                    view_contacts()
               case '3':
                    search_contact()
               case '4':
                    edit_contact()
               case '5':
                    delete_contact()
               case '6':
                    break
               case _:
                    print("Please choose from only from given options.")

main()