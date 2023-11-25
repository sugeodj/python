# sort files within a folder by file extension

import os
import shutil

# get current working directory
cwd = os.getcwd()

# get list of files in cwd
files = os.listdir(cwd)

# create a list of file extensions
extensions = []
for file in files:
    if os.path.isfile(file):
        extensions.append(file.split('.')[-1])

# remove duplicates
extensions = list(set(extensions))

# create folders for each extension
for extension in extensions:
    if not os.path.exists(extension):
        os.makedirs(extension)

# move files to their respective folders
for file in files:
    if os.path.isfile(file):
        shutil.move(file, file.split('.')[-1])

# print message
print('Files sorted by extension.')
