"""
 Challenge: Auto File Organizer with Watchdog

Goal:
- Monitor a folder (e.g., Downloads/Desktop)
- When a new file is added:
    - Move PDFs to /PDFs
    - Move Images to /Images
    - Move ZIP files to /Archives
    - Everything else goes to /Others

Teaches: Folder monitoring, real-time automation, event-driven design
Tools: watchdog, shutil, os
"""
import os
import shutil
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

DIRECTORY_MAP = {
    'PDFs': ['.pdf'],
    'Images': ['.jpg', '.jpeg', '.png'],
    'TextFiles': ['.txt']
}
TEMP_EXTENSIONS = {'.tmp', '.crdownload', '.part', '.download'}
WATCH_FOLDER = os.getcwd()

def find_folder(ext):
    for key, values in DIRECTORY_MAP.items():
        if ext in values:
            return key
    return 'Others'

class FileMoverHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        filepath = event.src_path
        ext = os.path.splitext(filepath)[1].lower()

        if ext in TEMP_EXTENSIONS:
            return
        
        # Wait for the file to be completely written (size stops changing)
        if not self._wait_until_stable(filepath):
            print(f"File {os.path.basename(filepath)} not stable — skipping.")
            return

        dest_folder = find_folder(ext)
        
        full_dest = os.path.join(WATCH_FOLDER, dest_folder)

        os.makedirs(full_dest, exist_ok=True)

        move_to = os.path.join(full_dest, os.path.basename(filepath))

        
        try:
            shutil.move(filepath, move_to)
            print(f"{os.path.basename(filepath)} moved to {dest_folder} folder.")
        except Exception as e:
            print("Failed to move the file. -", str(e))
    
       #To handle downloaded files after their temp file name change.
    def on_moved(self, event):
        if event.is_directory:
            return

        filepath = event.dest_path
        ext = os.path.splitext(filepath)[1].lower()

        if ext in TEMP_EXTENSIONS:
            return

        dest_folder = find_folder(ext)
        
        full_dest = os.path.join(WATCH_FOLDER, dest_folder)

        os.makedirs(full_dest, exist_ok=True)

        move_to = os.path.join(full_dest, os.path.basename(filepath))
        try:
            shutil.move(filepath, move_to)
            print(f"{os.path.basename(filepath)} moved to {dest_folder} folder.")
        except Exception as e:
            print("Failed to move the file. -", str(e))

    def _wait_until_stable(self, filepath, checks=3, delay=1):
        """Wait until file size stops changing."""
        last_size = -1
        for _ in range(checks):
            try:
                current_size = os.path.getsize(filepath)
            except FileNotFoundError:
                return False
            if current_size == last_size:
                return True
            last_size = current_size
            time.sleep(delay)
        return False

if __name__ == '__main__':
    print("Watching folder:", WATCH_FOLDER)
    event_handler = FileMoverHandler()
    observer = Observer()

    observer.schedule(event_handler, path=WATCH_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
