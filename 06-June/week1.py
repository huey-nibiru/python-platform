# FILE HANDLING & GAME DATA USING JSON


import os, time, json
from os.path import exists



# file handling is how we create, read update, and delete files
# there are three modes to open a file with
# 1. ("w") - writing to the file
# 2. ("a") - appending the file
# 3. ("r") - reading the file
# there are two ways to open and close files



# 1.) the open() & close() methods
# create a new file in write mode (w)
file = open("games.txt", "w")

# write something to the file
file.write("PLAYSTATION IS BEST!!!\n")

# close the file
file.close()


# 2.) use the "with open() as" method
# this opens the file, lets us do something, then closes the file immediately
# use 'a' to add text to the existing file
with open("games.txt", "a") as file:
    file.write("PS4 > XBOX\n")



    
# we can save data with json better than txt files
while True:
    os.system('clear')
    game = input("Game: ")
    console = input("Console: ")
    genre = input("Genre: ")
    g = {"game": game, "console": console, "genre":genre}

    
    # if the json file doesnt exist, create file and add empty list
    if exists("games.json") == False:
        with open("games.json", "w") as file:
            json.dump([], file)

            
    # if the file is empty, create a list in the file
    if os. stat("games.json").st_size == 0: 
        with open("games.json", "w") as file:
            data = json.dump([],file)

            
    # load existing info
    with open("games.json", "r") as file:
        # create a new list in the empty json file
        games = list(json.load(file))
        games.append(g)

        
    # merge new info
    with open("games.json", "w") as file:
        json.dump(games,file, indent=4)
    









