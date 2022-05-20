# SUMMER VACACTION

import os
import time
import random
from tqdm import trange


countries = ["mexico", "italy", "korea", "uganda",
            "morocco", "spain", "russia", "colombia"]


# print statements are to display info on the screen
print(".....VACATION OPTIONS......")


# we use a join to output a list in a certain format
countries_f = "\n".join(countries)
print(countries_f)


# give yourself a random amount of money 
cash = random.randint(0,5000)
inventory = ["wallet", "backpack", "suitcase"]


# select a country to move to
choice = input("\nSelect destination: ")
if choice in countries:
    price = random.randint(100,2000)
    if cash >= price:
        max_items = random.randint(1,10)
        if len(inventory) <= max_items:
            for i in trange(100):
                time.sleep(.1)
            os.system("clear")
            print("Location loaded.")
            time.sleep(1)
            print("Location:", choice)        
        else:
            print("You have too many items.")
    else:
        print("You do not have enough funds.")
        print("Price: $", price)
        print("Cash: $", cash)
             
else:
    print("Invalid Location...")


