# File Organizer

This Python script automatically organizes files in a specified directory by moving them into categorized subfolders based on their file extensions. It's a great tool for managing your downloads or any folder that collects miscellaneous files.

## Features

- **Real-time Monitoring**: Automatically detects and organizes new files as soon as they are created.
- **Customizable Categories**: Easily add or modify file categories and extensions to fit your needs.
- **Simple Setup**: Just modify the configuration to start organizing.

## Prerequisites

- Python 3.x
- `watchdog` package

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/file-organizer.git
   cd file-organizer
   ```

2. **Install dependencies**
   ```bash
   pip install watchdog
   ```

## Configuration

- Open the `file_organizer.py` script and update the following paths:
  - `WATCHED_FOLDER`: The directory you want to monitor. Use absolute paths.
  - `TARGET_FOLDER`: The directory where categorized subfolders will be created.

- Customize your file categories and extensions in the `FILE_CATEGORIES` dictionary if needed.

## Usage

Run the script using Python:

```bash
python file_organizer.py
```

The script will start monitoring the specified directory and automatically move files to their categorized subfolders.

## Customization

### Adding New File Categories

To add more file categories or file extensions, modify the `FILE_CATEGORIES` dictionary in the script:

```python
FILE_CATEGORIES = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    # Add your new categories and extensions here
}
```

## Troubleshooting

- **Permission Errors**: Ensure the script has appropriate read/write permissions for the directories.
- **Unsupported File Types**: Files with extensions not listed in `FILE_CATEGORIES` will not be moved.

## Contributing

Feel free to submit issues or fork the repository to contribute to the project.
