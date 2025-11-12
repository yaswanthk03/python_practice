"""
 Challenge: File Sorter by Type

Goal:
- Scan the current folder (or a user-provided folder)
- Move files into subfolders based on their type:
    - .pdf → PDFs/
    - .jpg, .jpeg, .png → Images/
    - .txt → TextFiles/
    - Others → Others/
- Create folders if they don't exist
- Ignore folders during the move

Teaches: File system operations, automation, file handling with `os` and `shutil`
"""
import os
import shutil

DIRECTORY_MAP = {
    'PDFs': ['.pdf'],
    'Images': ['.jpg', '.jpeg', '.png'],
    'TextFiles': ['.txt']
}

def find_destination_directory(file_name):
    file_extension = os.path.splitext(file_name)[1].lower()
    if file_extension == '.py':
        return 
    for folder, extensions in DIRECTORY_MAP.items():
        if file_extension in extensions:
            return folder
    return 'Others'

def sort_files(folder_path):
    for file in os.listdir(folder_path):
        if os.path.isfile(file):
            file_path = os.path.join(folder_path, file)
            dest_folder = find_destination_directory(file)
            
            if dest_folder:
                os.makedirs(dest_folder, exist_ok=True)
                dest_path = os.path.join(folder_path, dest_folder)
                shutil.move(file_path, os.path.join(dest_path, file))
                print(f'{file} moved to {dest_folder}')

if __name__ == '__main__':
    folder = input("Enter Folder name or leave it empty to process current working directory: ")    

    folder = folder or os.getcwd()

    if os.path.isdir(folder):
        sort_files(folder)
        print("Sorted successfully. ✅")
    else:
        print("Not a valid folder.")