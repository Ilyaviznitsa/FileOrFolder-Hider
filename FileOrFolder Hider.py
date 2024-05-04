# Filename: fileorfolder_hider.py

import os

# Prompt user to choose between hiding and unhiding
action = input("Do you want to hide or unhide a file/folder? (hide/unhide): ").strip().lower()

# Ask for the full path to the file or folder
path = input("Enter the full path of the file/folder to hide/unhide: ").strip()

if not os.path.exists(path):
    print("Error: The specified path does not exist.")
else:
    if action == "hide":
        # Hide the file/folder with the +h attribute
        os.system(f"attrib +h \"{path}\"")
        print(f"Successfully hid: {path} now you can close the program")
        input()
    elif action == "unhide":
        # Unhide the file/folder by removing the hidden attribute
        os.system(f"attrib -h \"{path}\"")
        print(f"Successfully unhid: {path} now you can close the program")
        input()
    else:
        print("Error: Invalid action. Please choose 'hide' or 'unhide'.")