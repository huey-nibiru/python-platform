"""
Project Name: ROCK PAPER SCISSORS
Concepts: random library, variables, loops, lists, conditions
Homework: make the game best 2 out of 3
"""

#importing module for random number generation
import random

# game assets. Create 
choices = ["rock", "paper", "scissors"]
player = False
cpu_score = 0
player_score = 0


# run the game
while True:
    computer = random.choice(choices)
    player = input("Rock, Paper or  Scissors?").lower()
    
    if player == computer:
        print("Tie!")
    
    
    # each if statement is similar. Copy paste to save time.


    # outcome 1
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
            cpu_score+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
    
    # outcome 2
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
            cpu_score+=1
        else:
            print("You win!", player, "covers", computer)
            player_score+=1
    
    # outcome 3 
    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
            cpu_score+=1
        else:
            print("You win!", player, "cut", computer)
            player_score+=1
    
    
    # end screen
    elif player=='End':
        print("Final Scores:")
        print("CPU:", cpu_score)
        print("Player:",player_score)
        break
