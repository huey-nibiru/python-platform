# DICE ROLLING

#importing module for random number generation
import random

#range of the values of a dice
min_val = 1
max_val = 6

#to loop the rolling through user input
roll_again = "y"

# loop the rolling until we decide to stop
while roll_again == "y":
    
    
    # generate 1st random integer from 1 to 6
    dice1 = (random.randint(min_val, max_val))
    
    # generate 2nd random integer from 1 to 6
    dice2 = (random.randint(min_val, max_val))

    # output the results
    print("Rolling The Dices...")
    print("Dice One:", dice1)
    print("Dice Two:", dice2)
    
    #asking user to roll the dice again. Any input other than yes or y will terminate the loop
    print("Type 'y' to roll again. Press enter to quit: ") 
    roll_again = input(">")
