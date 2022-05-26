"""
Project Name:  CARTOON CHARACTER PROFILE 
Concepts: dictionaries, loops, variables
Homework: add more cartoon characters
"""

# a dictionary holds info in keys and values
# we can create categories for each character (name, show, species, home)
# my cartoon characters
# c1 means character 1


c1 = {
    "name": "spongebob",
    "show": "spongebob squarepants",
    "species": "sponge",
    "home": "bikini bottom",
}

c2 = {
    "name": "patrick",
    "show": "spongebob squarepants",
    "species": "starfish",
    "home": "bikini bottom",
}

c3 = {
    "name": "squidward",
    "show": "spongebob squarepants",
    "species": "octopus",
    "home": "bikini bottom",
}

# store every character in a list
characters = [c1,c2,c3]
num_chars = len(characters)

print("There are", num_chars, "characters in my list \n")

for c in characters:
    name = c["name"]
    species = c["species"]
    home = c["home"]
    print(name, "is a", species, "that lives in", home)



