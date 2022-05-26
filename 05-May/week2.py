"""
Project Name: RECIPE GENERATOR
Concepts: lists, loops, random, functions conditions
Homework: add more foods 
"""

from random import choice
from os import system
from time import sleep
from tqdm import tqdm


def load_bar():
    for i in tqdm(range(10)):
        sleep(.1)

load_bar()

meats = ["chicken", "fish", "steak"]
veggies = ["broccoli", "cabbage", "carrot"]
spices = ["chili", "garlic", "pepper"]
sauces = ["tomato sauce", "bbq sauce", "hot sauce"]
sides = ["fries", "nuggets", "rice"]


# make the recipe
recipe = []
for food in [meats, veggies, spices, sauces, sides]:
    food = choice(food)
    recipe.append(food)


# DISPLAY OUR RECIPE
print("New recipe Loaded...\n")
for food in recipe:
    sleep(.1)
    print(">",food)


