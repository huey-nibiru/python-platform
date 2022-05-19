import os
import random
import time


# CREATE THE PLAYER VARIABLES
p1 = "X"
p2 = "O"



# CREATE THE GAME BOARD
row1 = ["1", "2", "3"]
row2 = ["4", "5", "6"]
row3 = ["7", "8", "9"]
board = [row1, row2, row3]



# SHOW THE BOARD
def show_board():
  time.sleep(1)
  os.system('clear')
  for row in board:
    print(" | ".join(row))
    print("----------")
show_board()




# CREATE THE SOLUTIONS
def scan_solutions(p):
  
  h1 = board[0][0]==p and board[0][1]==p and board[0][2]==p
  h2 = board[1][0]==p and board[1][1]==p and board[1][2]==p
  h3 = board[2][0]==p and board[2][1]==p and board[2][2]==p
  

  v1 = board[0][0]==p and board[1][0]==p and board[2][0]==p
  v2 = board[0][1]==p and board[1][1]==p and board[2][1]==p
  v3 = board[0][2]==p and board[1][2]==p and board[2][2]==p

   
  d1 = board[0][0]==p and board[1][1]==p and board[2][2]==p
  d2 = board[2][0]==p and board[1][1]==p and board[0][2]==p

  solutions = [h1,h2,h3,v1,v2,v3,d1,d2]
  if True in solutions:
    show_board()
    print(p + " WINS")
    exit(0)


# START THE GAME
player = random.choice([p1,p2])
choices = list(range(1,10))


while True:
  print("It is " + player + " Turn.")
  choice = int(input("choose a spot: "))
  if choice in choices:
      print(str(choice) + " selected.")
      
      # Use copy and paste for each elif then change the numbers
      if choice == 1:
        board[0][0] = player # reassign board number to an X or O
        choices.remove(1)    # dont allow this spot to be chosen again  
    
      elif choice == 2:
        board[0][1] = player # reassign board number to an X or O
        choices.remove(2)    # dont allow this spot to be chosen again  

      elif choice == 3:
        board[0][2] = player # reassign board number to an X or O
        choices.remove(3)    # dont allow this spot to be chosen again  
    
      elif choice == 4:
        board[1][0] = player # reassign board number to an X or O
        choices.remove(4)    # dont allow this spot to be chosen again  

      elif choice == 5:
        board[1][1] = player # reassign board number to an X or O
        choices.remove(5)    # dont allow this spot to be chosen again  

      elif choice == 6:
        board[1][2] = player # reassign board number to an X or O
        choices.remove(6)    # dont allow this spot to be chosen again  
      
      elif choice == 7:
        board[2][0] = player # reassign board number to an X or O
        choices.remove(7)    # dont allow this spot to be chosen again  
      
      elif choice == 8:
        board[2][1] = player # reassign board number to an X or O
        choices.remove(8)    # dont allow this spot to be chosen again  

      elif choice == 9:
        board[2][2] = player # reassign board number to an X or O
        choices.remove(9)    # dont allow this spot to be chosen again  

      scan_solutions(player)
    
      if player == p1:
        player = p2
      elif player == p2:
        player = p1
  else:
    print("INVALID SPOT")
  show_board()
    