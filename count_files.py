""" 
A program to count the total number of files in a given directory,
it may have sub directories as well.
"""

import os
import sys

class CountFilesAndFolders():
    """Counts all files and folders given a directory"""
    
    def __init__(self, file_path):
        """Setting attributes."""
        self.file_path = file_path
        self.file_names = []
        self.folder_names = []

    def display_files(self):
        """Displays all files in the list passed in"""
        if self.file_names:
            for file_name in self.file_names:
                print(file_name)

    def display_folders(self):
        """Displays all folders in the list passed in."""
        if self.folder_names:
            for folder_name in self.folder_names:
                print(folder_name)
    
    def generate_path(self, start_path, file_name):
        """Generate a path to get to the folder."""
        current_path = None

        if file_name and start_path:
            if not start_path.endswith("/"):
                current_path = start_path + "/" + file_name
            else:
                current_path = start_path + file_name
        return current_path

    def gather(self, file_path):
        """Gathers all files and directory of a given a valid folder."""
        files_or_folders = None
        folders = []

        if os.path.isdir(file_path):
            try:
                files_or_folders = os.listdir(file_path)
            except PermissionError:
                pass
                #print("Access not granted, could not access " + file_path)
            else:
                if files_or_folders:
                    for file_or_folder in files_or_folders:
                        # Generating current file path.
                        file_or_folder = self.generate_path(file_path, file_or_folder) 
                        # Checking for files.
                        if os.path.isfile(file_or_folder):
                            if file_or_folder not in self.file_names: 
                                self.file_names.append(file_or_folder)
                        # Checking for folder.
                        elif os.path.isdir(file_or_folder):
                            if file_or_folder not in self.folder_names: 
                                # ignoring .git folders.
                                if os.path.basename(file_or_folder) != ".git":
                                    self.folder_names.append(file_or_folder)
                                    folders.append(file_or_folder)
        # Gathering all folders and files in all sub directories.
        if folders:
            for folder in folders:
                self.gather(folder)
             
    def print_total(self):
       """Print total number of files and folders."""
       print("Total files: " + str(len(self.file_names)))
       print("Total folders: " + str(len(self.folder_names)))

def confirm_validity(file_path):
    """Confirms the folder exists and is a directory"""
    exists = False

    if os.path.exists(file_path) and os.path.isdir(file_path):
        exists = True

    return exists

def count():
    """
    Create an object of the class CountFilesAndFolders and proceed
    to count the files after prompting for a file path."""
    
    if len(sys.argv) < 2:
        file_path = input("Enter a file path: ").strip()
        if confirm_validity(file_path):
            test = CountFilesAndFolders(file_path)
            test.gather(test.file_path)
            test.print_total()
        else:
            print("File path not valid")
    else:
        file_path = str(sys.argv[1])
        if confirm_validity(file_path):
            test = CountFilesAndFolders(file_path)
            test.gather(test.file_path)
            test.print_total()
        else:
            print("File path not valid")

try:
    count()
except KeyboardInterrupt:
    print("Stopped happy now :(")
else:
    pass
    
