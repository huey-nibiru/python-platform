# INTRO TO FILE HANDLING 

# import os to allow us to clear the screen
import os

# file handling is how we create, read, update, and delete files
# there are 3 modes to open files with
# 1. ("w") - write to the file - (overwrite existing data)
# 2. ("a") - append to the file - (adds to existing data)
# 3. ("r") - read the file - (loads existing data)


# There are two ways to open and close files 
#1. the open() and close() method
#2. with statement


# open a new file
file = open("games.txt", "w")

# write to the file
file.write("...MY FAVORITE GAMES...\n")

# close the file
file.close()

# with statements dont need a close() method
# open the file with mode 'r' to read the contents of the file
with open("games.txt", "r") as file:
    print(file.read())


# create a loop that lets us keep adding favorite games to our file
while True:

    # enter the name of a game you like
    print("Type 'quit' to stop")
    game = input("Enter a game you like: ")
    
    # stop the loop if you enter 'quit'
    # this must be before we add the game to the file to prevent it from being added 
    if game == "quit":
      break

    # use the with statement with mode 'a' to quickly add the game to the file
    # use \n to keep each game on a new line
    with open("games.txt", "a") as file:
        file.write(" - " + game + "\n")
        


# clear the screen and display the contents of the file
os.system("clear")
with open("games.txt","r") as file:
    print(file.read())



