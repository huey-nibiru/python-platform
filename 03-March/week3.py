
"""
Project Name: FOOD STORE 
Concepts: time lib, os lib, dictionaries, file io, loops
Homework: add more items to the menu
"""
import time, os


menu = {
  "beef": 2.99,
  "milkshake": 4.99,
  "chips": 0.99,
  "mac & cheese": 6.99,
  "ham & turkey sandwich": 4.99,
  "ice cream": 5.99,
  "bagel": 1.99,
}


# open a new file 
file = open("receipt.txt", "w")
total = 0
file.write("RECEIPT\n\n")
#file.close()


#theres three modes we use
# w - write
# a - append
# r - read

while True:
  time.sleep(1)
  os.system("clear")
  
  print("...DELI....")
  # DISPLAY THE FOOD INFO
  for i in menu:
    price = (menu[i])
    print(i + "....$" + str(price))
    

  # CHOOSE AN ITEM
  choice = input("\nchoose an item >")
  if choice in menu:
    price = (menu[choice])
    print("that will be $" + str(price) )
    file.write(choice + "...$" + str(price) + "\n")
    total += price
    break
  else: 
    print("we don't have that item.")
  
  
# ADD MORE ITEMS TO THE CART AND QUIT
while True:
  more = input("\nWhat else? (type 'nothing' to quit)")  
  if more == "nothing":
    break
  
  elif more in menu:
    price = (menu[more])
    print("that will be $" + str(price))
    file.write(more + "...$" + str(price) + "\n")
    total += price
  
  else:
    print("Choose a new item or type 'no' to quit.")
os.system("clear")

