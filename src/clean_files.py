#!/usr/bin/python

# Example run command to print, but not alter, file names: python clean_files.py C:\Users\zahus\Documents\Dev\SachiFileCleanupScript false
# Example run command to alter file names: python clean_files.py C:\Users\zahus\Documents\Dev\SachiFileCleanupScript true

import os
import sys

class File:
    def __init__(self, filename, subdir):
        self.filename = filename
        self.subdir = subdir

    def filename(self):
        return self.filename

    def alter_filename(self, new_filename):
        self.altered_filename = new_filename
        self.altered = True

    def altered(self):
        return self.altered

    def full_path(self):
        return os.path.join(subdir, self.filename)

    def altered_path(self):
        return os.path.join(subdir, self.altered_filename)

    def save_changes(self):
        print("Making file rename")

        os.rename(self.full_path(), self.altered_path())
        self.filename = self.altered_filename


class FileAlteration:
    def __init__(self, file):
        self.file = file

    def transform(self, filename):
        print("Transform not implemented by subclass")

    def alter(self):
        original_filename = self.file.filename
        modified_filename = self.transform(original_filename)

        if modified_filename != original_filename:
            print("Detected a difference between the two file names", original_filename, modified_filename)

            self.file.alter_filename(modified_filename)


class CleanDashes(FileAlteration):
    def __init__(self, file):
        super().__init__(file)

    def transform(self, filename):
        return filename.replace('-', '_')


class RemoveMiddleDots(FileAlteration):
    def __init__(self, file):
        super().__init__(file)

    def transform(self, filename):
        return filename.replace('•', '_')



if len(sys.argv) < 2:
    print("Missing starting directory argument")
    exit()
else
    starting_dir = sys.argv[1]

if len(sys.argv) < 3:
    should_modify = False
else
    should_modify = sys.argv[2] == 'true'

print(f"Running script starting at ({starting_dir}), should_modify set to {should_modify}")

for subdir, dirs, files in os.walk(starting_dir): # parse through file list in the folder "test"
    for filename in files:
        file = File(filename, subdir)
        CleanDashes(file).alter()
        RemoveMiddleDots(file).alter()

        if file.altered == True:
            print("Modified file: ", file.full_path())
            if should_modify:
                file.save_changes()
