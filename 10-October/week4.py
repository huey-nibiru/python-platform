"""
Project Name:  NUMBER GUESSER
Concepts: variables, loops, error handling
Homework: make the program print a congrats message if the number is guessed in under 5 tries
"""



# allows us to use random numbers and random choice
import random

# allows us to clear the screen 
import os

# allows us to pause the screen
import time

# choose a random number between 0 and 100 [review variables and randint]
randomNumber = random.randint(0, 100)

# keep track of how many tries it will take us
tries = 0
    
# while loop will keep the program running [explain why the loop is needed]
while True: 
    
    # pause the screen for a second and clear
    time.sleep(1)
    os.system("clear")
  
    # try/except will keep the program from exiting if a letter is entered
    try:
    
        # let the user know the numbers to guess between
        print("Guess a number between 0 and 100")
        
        # guess is a variable that holds a numerical input
        guess = int(input('>>> '))

        # if the user guesses correctly, end loop with break
        if guess == randomNumber:
            print('correct!')

            # display number of tries
            print("It took you", tries, "tries")
            break 

        # if the guess is too low, display a message
        elif guess < randomNumber:
            print('Guess higher')

        # if the guess is too high, display a message
        elif guess > randomNumber:
            print('guess lower')
        
        # tally the amount of tries
        tries += 1

    # if the user enters a non-number, display a message
    except ValueError:
        print('Enter an number, not a letter!')
