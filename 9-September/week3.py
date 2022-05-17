# a list is a data structure that holds multiple
# values of data that can be modified
# you can add and remove items from a list
# each list is created using square brackets
languages = ["python", "c++", "java", "html", "sql", "javascript", "swift", "solidity"]


# we can find out how many items in a list using the len() method
num_languages = len(languages)
print("There are", num_languages, "languages in my list")



# we can access values in a list by calling the list name with square brackets after, and an index inside the brackets
# the first element of a list is always 0
first = languages[0]
print("The first language in my list is", first)


# the last element of a list is always -1
# you can start counting the elements of a list backwards starting from -1
last = languages[-1]
print("The last language in my list is", last)


# we can access parts of a list using list slicing
# you start at a selected index, and end at a selected index 
# we use this format:  list_name[start:stop]
# if we want to start at the beginning, leave start empty
# if we want to run all the way thru the list, leave the stop empty
start = 0
end = num_languages
stride = 2
print("this prints every 2 elements")
print(languages[start:end:stride])


# if i want to split the list in half
# i can end the slice halfway
end = num_languages // 2 
print(languages[start:end]) 


import os
os.system("clear")


# a dictionary is similar to a list except we use
# curly brackets to define one, and ever element has
# a key and a value
lang_uses = {"python":"back-end development and data",
            "c++":"game development", 
            "HTML":"front-end development",
            "javascript":"front-end development",
            "java":"systems development",
            "swift":"ios development",
            "solidity":"blockchain development"
            }

# to find a value of a key, use the name of the dictionary
# and the key itself like this
key1 = list(lang_uses.keys())[0]
value1 = lang_uses["python"]
print(key1 + " is used for " + value1)

os.system("clear")

# display the keys and values of the whole dictionary
# using a for loop
for lang in lang_uses:
    use = lang_uses[lang]
    print(lang + " is used for " + use)


#  this is how we add to a dictionary
lang_uses["c#"] = "game development"


# delete a key/value
del lang_uses["python"]






























