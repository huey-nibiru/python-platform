# DICTIONARIES REVIEW

import os

# dictionaries are used to store data in key/value pairs
# dictionaries often represent an object

# how to create a dictionary 
employee = {}

# add data to your dictionary
employee["name"] = "Daniel"
employee["job"] = "Fashion Designer"
employee["company"] = "Nike"

# print the full dictionary
print(employee)

# clear the screen
input("\nPRESS ENTER")
os.system("clear")

# how to access a variable from your dictionary
print("Hello my name is", employee["name"])
print("I am a", employee["job"])
print("I work for", employee["company"])

# change a value 
employee["name"] = "Danny"
print("you can just call me", employee["name"])













