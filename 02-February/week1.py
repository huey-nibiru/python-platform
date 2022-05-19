# RESTAURANT 

# allows us to clear the screen
import os

# allow us to pause the screen
import time

# create the name for the restaurant/store
name = "Sams Smoothies"

# create a variable to hold the total
total = 0

# create a list to hold the items bought 
cart = []

# create a dictionary to store the menu, add up to 20 items
menu = { }
menu["banana"] = 10
menu["orange"] = 11
menu["veggie"] = 9
menu["vanilla"] = 17
menu["mango"] = 7
menu["apple"] = 3
menu["raspberry"] = 5



# create a function that can display the menu in a nice format
def show_menu():
  print(".........." + name + "..........")
  for flavor in menu:
    price = str(menu[flavor])
    print(flavor + "....$" + price)
  
  
  
# use a while loop to keep the program running 
while True:
  
  # clear the screen
  time.sleep(1)
  os.system("clear")
  
  # show the menu
  show_menu()
  
  # choose a flavor
  choice = input("\nSelect a flavor (type 'quit' to stop) :")
  
  # verify if the choice is in the menu, add item to cart
  if choice in menu:
    price = menu[choice]
    cart.append(choice)
    print("That will be $" + str(price))
    total += price
  
  # if the user enters "quit" the loop will end & show the items bought 
  elif choice == "quit":
    os.system("clear")
    print("....RECIEPT......")
    for item in cart:
      print(">",item)
      
    # display the total
    print("Your total is $" + str(total))
    break
  
    

    
  
  
  



















