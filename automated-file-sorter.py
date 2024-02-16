import os, shutil

# Directory to sort files

path = r"C:/Users/radlm/Downloads/"

files = os.listdir(path)

# Check if folder exists, if not create one

folder_names = ["pdf files", "image files", "data files",]

for folder in folder_names:
    if not os.path.exists(path + folder):
        os.makedirs((path + folder))

# Sort files by their extension

for file in files:
    # Move PDF files to "pdf files" folder
    if ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file)

    # Move Excel files to "data files" folder
    elif ".xlsx" in file and not os.path.exists(path + "data files/" + file):
        shutil.move(path + file, path + "data files/" + file)

    # Move JPG files to "image files" folder
    elif ".jpg" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
        
    # If file type not recognized, print a message
    # Ensuring it's a file before printing to avoid printing for folders
    elif os.path.isfile(path + file):
        print(file + " this file type is not included.")