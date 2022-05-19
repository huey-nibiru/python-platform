# MINECRAFT 

# allows us to clear the screen 
import os

# allows us to pause the screen
import time




# variables store information. Name your variables what they represent
# each variable has a data type ["review data types"]
name = "Steve"
age = 20
tool = "pickaxe"
location = "overworld"




# we can store multiple values in a list. lists use square brackets
maps = ["skyblock", "parkour school", "funland", "future city"]
tools = ["sword", "compass", "fishing rod", "shovel"]



# print statements will display information
print("Hi my name is", name, "and i am", age, "years old.")
print("I am currently in", location)



# create function to show each world and change the player location
def change_loc():
    os.system("clear")
    print("...WORLDS...")
    for world in maps:
        print(world)
    choice = input(">>>")
    if choice in maps:
        location = choice
    else:
        print("Invalid location")
    
def change_tool():
    os.system("clear")
    print("...TOOLS...")
    for tool in tools:
        print(tool)
    choice = input(">>>")
    if choice in tools:
        location = choice
    else:
        print("Invalid tols")


# create a function that serves as a menu 
def menu():
    print("Name:", name)
    print("Tool:", tool)
    print("Location:", location, "\n")


    # create options
    print("1. Change location")
    print("2. Change tool")
    print("3. Exit")


    # create user input
    choice = input(">>>")


    # if statements control what happens for each choice
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

