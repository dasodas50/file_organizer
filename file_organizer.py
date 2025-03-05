import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configuration for file extensions and their corresponding folders
FILE_CATEGORIES = {
    'Documents': ['.pdf', '.docx', '.txt','.xlsx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    # Add more categories and extensions as needed
}

# Path to watch
WATCHED_FOLDER = '/path/to/watch/folder'  # Change this to your folder. If you use Windows the path nust look like this  C://Users//your_username//Downloads//
# Path to target folder.
TARGET_FOLDER = '/path/to/target/folder' # If you use Windows the path nust look like this  C://example//target_folder//

def get_target_folder(extension):
    """Get the target folder based on file extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return None

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        """Handle the event when a file is created in the watched folder."""
        if event.is_directory:
            return

        file_path = event.src_path
        _, extension = os.path.splitext(file_path)
        target_folder_name = get_target_folder(extension)

        if not target_folder_name:
            print(f'Unsupported file type for file: {file_path}')
            return
        
        target_folder_path = os.path.join(TARGET_FOLDER, target_folder_name)  
        
        os.makedirs(target_folder_path, exist_ok=True)

        try:
            shutil.move(file_path, os.path.join(target_folder_path, os.path.basename(file_path)))
            print(f"Moved file {os.path.basename(file_path)} to {target_folder_name}")
        except shutil.Error as e:
            print(f'Error moving file: {e}')
        except PermissionError as pe:
            print(f"Permission error: {pe}")

def main():
    observer = Observer()
    event_handler = FileHandler()
    
    observer.schedule(event_handler, WATCHED_FOLDER, recursive=False)
    observer.start()

    print(f"Monitoring folder: {WATCHED_FOLDER}")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()