# TREE GARDEN GAME


# spell a word correctly to plant a tree. 
# if you spell a word wrong, you lose
# if it takes you more than 3 seconds to type the word you lose
# plant as many trees as possible


# allows us to use random numbers and random choice
import random

# allows us to clear the screen 
import os

# allows us to pause the screen
import time


# create a wordbank and use emojies for the trees 
wordbank = [""]
tree = "🌲"


# create a list for each row and the garden
row = []
garden = []


# while loops are used to run the whole game
while True:
    os.system("clear")
    
    # display the garden. (rows must be full)
    for each_row in garden:
        print(" ".join(each_row))
    
    # start the timer for entry
    start = time.time()
    word = random.choice(wordbank)
    print("Type the word", word)
    entry = input(">>>")
    end = time.time()
    time_limit = int(end - start)

    # set the time limit to five seconds
    # if the user spells the word wrong, end program
    if time_limit > 5:
        print("YOU LOSE")
        break
    
    # wrong spelling
    elif word != entry:
        print("YOU LOSE")
        break
    
    # add new tree to garden
    else:
        row.append(tree)

        # only let garden have rows of 5
        if len(row) == 5:
            garden.append(row)
            row = []


# display the number of trees planted
num_trees = len(garden) * 5
print("You planted", num_trees, "trees.")