# ANIMAL SHELTER

import os
import time

print("Animal Shelter")

# create a variable for the amount of money
# variables must be named properly
money = 100

# every variable has a data type
# money is an integer data type

# dictionaries hold info in key/value pairs
# create dictionaries with curly brackets
dog1 = {}

# we can add key/value pairs to the dictionary
dog1["name"] = "greaseball"
dog1["breed"] = "bulldog"
dog1["age"] = 4
dog1["weight"] = 60
dog1["price"] = 70


dog2 = {}
dog2["name"] = "iron mike"
dog2["breed"] = "pitbull"
dog2["age"] = 3
dog2["weight"] = 30
dog2["price"] = 40





# create the shelter 
# lists can hold info; create lists with []
shelter = [dog1, dog2]

while True:
    time.sleep(1)
    os.system("clear")
    # create a menu using print statements and input 
    print("Wallet: $", money)
    print("1. View all animals")
    print("2. Adopt an animal")
    choice = input(">>>")
    os.system("clear")
    
    # access the variable holding each animal
    if choice == "1":
    
        # loop through the shelter variable
        for animal in shelter:
            print("Name:",animal["name"])
            print("Age:",animal["age"])
            print("Breed:",animal["breed"])
            print("Weight:",animal["weight"])
            print("Price: $", animal["price"])
            print("\n") # create a line of space
        input("Press enter to return")

    
    elif choice == "2":
        for animal in shelter:
            print("Name:",animal["name"])
            print("Price: $", animal["price"])
            print("\n") 
        choice = input("Choose your new pal: ")
    
        # validate whether the animal exists
        try:
            for animal in shelter:
                if animal["name"] == choice:
                    if money > animal["price"]:
                        money -= animal["price"]
                        print(choice, "is your new friend!")
                        shelter.remove(animal)
                    else:
                        print("Not enough money.")
    
    
        except:
            print("Animal doesnt exist.")
            
        
    
