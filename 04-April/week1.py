"""
Project Name: PERSON PROFILE 
Concepts: os lib, dictionaries, variables
Homework: add more categories to the person and display each in a sentence
"""


import os

# dictionaries are used to store data in key/value pairs
# dictionaries often represent an object

# how to create a dictionary 
person = {}

# add data to your dictionary
person["name"] = "Daniel"
person["job"] = "Fashion Designer"
person["company"] = "Nike"

# print the full dictionary
print(person)

# clear the screen
input("\nPRESS ENTER")
os.system("clear")

# how to access a variable from your dictionary
print("Hello my name is", person["name"])
print("I am a", person["job"])
print("I work for", person["company"])

# change a value 
person["name"] = "Danny"
print("you can just call me", person["name"])













