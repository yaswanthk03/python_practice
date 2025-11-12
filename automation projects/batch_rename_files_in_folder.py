"""
Challenge: Batch Rename Files in a Folder

Goal:
- Scan all files in a selected folder
- Rename them with a consistent pattern:
    e.g., "image_1.jpg", "image_2.jpg", ...
- Ask the user for:
    - A base name (e.g., "image")
    - A file extension to filter (e.g., ".jpg")
- Preview before renaming
- Optional: allow undo (save original names in a file)

Teaches: File iteration, string formatting, renaming, user input
"""
import os

def rename(folder_name, base_name, file_extension):
    base_cnt = 1
    rename_preview = []
    for file in os.listdir(folder_name):
        if os.path.isfile(file):
            ext = os.path.splitext(file)[1]
            
            if ext == file_extension:
                new_name = f'{base_name}_{base_cnt}{ext}'
                rename_preview.append((file, new_name))
                print(f'{file} -> {new_name}')
                base_cnt += 1
    
    choice = input("Enter (y) to save the newly named files: ").strip().lower()

    if choice == 'y':
        for prev, new in rename_preview:
            os.rename(prev, new)
        print("File names renamed.✅")
        return
    print("File name rename stopped.")

def main():
    folder = input("Enter folder name or leave blank for pwd: ")
    folder = folder or os.getcwd()
    if not os.path.isdir(folder):
        print("Folder doesn't exists.")
        return
    while not (base_name := input("Enter base name: ").strip()):
        print("Base name cannot be empty.")
    
    while True:
        extension = input("Enter a file extension like('.pdf'): ")
        if not extension or extension[0] != '.':
            continue
        break
        
    rename(folder, base_name, extension)

main()