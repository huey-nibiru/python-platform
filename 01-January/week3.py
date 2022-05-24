# MINECRAFT PLAYER

# allows us to clear the screen 
import os

# allows us to pause the screen
import time


# dictionaries store information in key/value pairs. 
# Name your keys what they represent, then set it equal to something
# each variable has a data type ["review data types"]
player = {}
player["name"] = "Steve"
player["age"] = 20
player["tool"] = "pickaxe"
player["location"] = "overworld"




# we can store multiple values in a list. lists use square brackets
maps = ["skyblock", "parkour school", "funland", "future city"]
tools = ["sword", "compass", "fishing rod", "shovel"]



# show each world and change the player location
def change_loc():
    os.system("clear")
    print("...WORLDS...")
    for world in maps:
        print(world)
    choice = input(">>>")
    if choice in maps:
        player["location"] = choice
    else:
        print("Invalid")
    
# cycle between differetn tools
def change_tool():
    os.system("clear")
    print("...TOOLS...")
    for tool in tools:
        print(tool)
    choice = input(">>>")
    if choice in tools:
        player["tool"] = choice
    else:
        print("Invalid")


# create a function that serves as a menu 
def menu():
    print("Name:", player["name"])
    print("Tool:", player["tool"])
    print("Location:", player["location"], "\n")


    # create options
    print("1. Change location")
    print("2. Change tool")
    print("3. Exit")


    # create user input
    choice = input(">>>")


    # control what happens for each choice
    if choice == "1":
        change_loc()
    elif choice == "2":
        change_tool()
    elif choice == "3":
        exit(0)
    else:
        print("invalid")



# use a while loop to run the program
while True:
    time.sleep(1)
    os.system("clear")
    menu()

