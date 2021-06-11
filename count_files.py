""" 
A program to count the total number of files in a given directory,
it may have sub directories as well.
"""

import os

class CountFilesAndFolders():
    """Counts all files and folders given a directory"""
    
    def __init__(self, file_path):
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
            current_path = start_path + file_name
        return current_path

    def gather(self, file_path):
        """Gathers all files and directory of a given a valid folder."""
        
        if os.path.isdir(file_path):
            files_or_folders = os.listdir(file_path)
        if files_or_folders:
            for file_or_folder in files_or_folders:
                # Generating current file path              
                file_or_folder = self.generate_path(file_path, file_or_folder) 
                # Checking for files
                if os.path.isfile(file_or_folder):
                    if file_or_folder not in self.file_names: 
                        self.file_names.append(file_or_folder)
                # Checking for folder
                elif os.path.isdir(file_or_folder):
                    if file_or_folder not in self.folder_names: 
                        self.folder_names.append(file_or_folder)

file_path = "/home/max/Desktop/python_work/"
test = CountFilesAndFolders(file_path)
test.gather(test.file_path)
print("Files: ")
test.display_files()
print("\n")
print("Folders: ")
test.display_folders()
