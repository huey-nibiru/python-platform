import os, json
from os.path import exists


# file handling is how we create, read, update, and delete files
# there are 3 modes to open files with
# 1. ("w") - write to the file - (overwrite existing data)
# 2. ("a") - append to the file - (adds to existing data)
# 3. ("r") - read the file - (loads existing data)

# There are two ways to open and close files 
#1. the open() and close() method
#2. with statement

# open() method
file = open("games.txt", "w")

# write to the file
file.write("Playstation is the best.\n")

# close() method [mandatory]
file.close()

# with statements dont need a close() method
with open("games.txt", "r") as file:
    print(file.read())



