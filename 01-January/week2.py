# ROCK PAPER SCISSORS

import random

# game assets. Create 
choices = ["rock", "paper", "scissors"]

player = False
cpu_score = 0
player_score = 0



while True:
    computer = random.choice(choices)
    player = input("Rock, Paper or  Scissors?").lower()
    

    if player == computer:
        print("Tie!")
    

    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
            cpu_score+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
    

    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
            cpu_score+=1
        else:
            print("You win!", player, "covers", computer)
            player_score+=1
    
    # 
    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
            cpu_score+=1
        else:
            print("You win!", player, "cut", computer)
            player_score+=1
    
    
    # use f strings to display variables in text 
    elif player=='End':
        print("Final Scores:")
        print("CPU:", cpu_score)
        print("Player:",player_score)
        break
