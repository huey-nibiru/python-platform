# VIDEO GAME STORE


# allows us to clear the screen 
import os

# allows us to pause the screen
import time

# give a name to the store
store_name = "gamestop"
with open("receipt.txt", "w") as file:
    file.write("....." + store_name + "......\n")

# create a menu of games and their prices
menu = {}
menu["call of duty mw3"] = 45
menu["gta v"] = 50
menu["spiderman"]= 55
menu["resident evil village"]=40
menu["call of duty mw3"] = 50



# create function to display games & prices
def display_menu():
    for game in menu:
        price = str( menu[game] )
        print(game + ".....$" + price)


# keep track of the total
total = 0 


# create function to buy games
def buy_games():
    global total
    os.system('clear')
    print("........" + store_name + "...........")
    display_menu()
    choice = input("\nselect a game:")

    # if you select a game in the menu, complete the purchase
    if choice in menu:
        # tally the price
        price = menu[choice]
        total += price
        print("That will be $" + str(price))
        time.sleep(1)

        # write the receipt to a file
        with open("receipt.txt", "a") as file:
            file.write(choice + "\n")
          
    elif choice == "quit":
        # write the total to the reciept
        with open("receipt.txt", "a") as file:
            file.write("\nTotal: $" + str(total))
        os.system("clear")
        exit(0)
        

    else:
        # input validation
        print("invalid choice. check spelling")
        time.sleep(1)
  

# run the program in a while loop
while True:
  buy_games()
  
  
  
  
  
  
  
  
  





    
    






