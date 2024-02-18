import os
import shutil
from pathlib import Path

# Directory to sort files
path = Path(r"C:/Users/radlm/Downloads/")

# Define file types and corresponding folders
file_types = {
    "pdf": "pdf files",
    "xlsx": "data files",
    "jpg": "image files",
    "png": "image files",
    # Add more file types here if needed
}

# Check if folders exist, if not create them
for folder in set(file_types.values()):
    (path / folder).mkdir(parents=True, exist_ok=True)

# Sort files by their extension
for file in path.iterdir():
    if file.is_file():
        extension = file.suffix[1:].lower()  # Get file extension without dot
        if extension in file_types:
            dest_folder = path / file_types[extension]
            if not (dest_folder / file.name).exists():
                shutil.move(file, dest_folder / file.name)
        else:
            print(f"{file.name} this file type is not included.")
