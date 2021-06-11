""" 
A program to count the total number of files in a given directory,
it may have sub directories as well.
"""

import os

class CountFilesAndFolders():
    """Counts all files and folders given a directory"""
    
    def __init__(self, file_path):
        self.file_path = file_path
        file_path = "/home/max/Desktop/python_work/"
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
    
    def generate_path(self, file_name):
        """Generate a path to get to the folder."""
        if file_name:
            os.path.join(self.file_path + "file_name")

        pass

    def gather(self):
        """Gathers all files and directory of a given a valid folder."""
        
        if os.path.isdir(self.file_path):
            files_or_folders = os.listdir(self.file_path)
        if files_or_folders:
            for file_or_folder in files_or_folders:
                # Checking for files
                if os.path.isfile(file_or_folder):
                    if file_or_folder not in self.file_names: 
                        self.file_names.append(file_or_folder)
                        print(file_or_folder)
                # Checking for folder
                elif os.path.isdir(file_or_folder):
                    if file_or_folder not in self.folder_names: 
                        self.folder_names.append(file_or_folder)

    print("Files: ")
    display_files(file_names)
    print("\n")
    print("Folders: ")
    display_folders(folder_names)
