""" 
A program to count the total number of files/directories in a 
given directory, it may have sub directories as well, 
hidden file/directories are counted.
"""

import os
import sys

class CountFilesAndFolders():
    """Counts all files and folders given a directory"""
    
    def __init__(self, file_path):
        """Setting attributes."""
        self.file_path = file_path
        self.file_count = 0
        self.folder_count = 0
            
    def gather(self):
        """Gathers all files and directory of a given a valid folder."""
       
        for current_file, sub_folders, file_names in os.walk(self.file_path):
            if ".git" not in current_file:
                self.file_count += len(file_names)
                self.folder_count += len(sub_folders)
             
    def print_total(self):
        """Print total number of files and folders."""
        print("Total files: " + str(self.file_count))
        print("Total folders: " + str(self.folder_count))


def confirm_validity(file_path):
    """Confirms the folder exists and is a directory"""
    exists = False

    if os.path.exists(file_path) and os.path.isdir(file_path):
        exists = True

    return exists

def count():
    """
    Create an object of the class CountFilesAndFolders and proceed
    to count the files after prompting for a file path.
    """
    
    if len(sys.argv) < 2:
        file_path = input("Enter a file path: ").strip()
        if confirm_validity(file_path):
            test = CountFilesAndFolders(file_path)
            test.gather()
            test.print_total()
        else:
            print("File path not valid")
    else:
        file_path = str(sys.argv[1])
        if confirm_validity(file_path):
            test = CountFilesAndFolders(file_path)
            test.gather()
            test.print_total()
        else:
            print("File path not valid")

try:
    count()
except KeyboardInterrupt:
    print("Stopped happy now :(")
else:
    pass
    
