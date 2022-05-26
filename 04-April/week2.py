"""
Project Name: FRUIT BASKET 
Concepts: lists, built in methods
Homework: add more fruits to the basket
"""

# a list is a data type that holds multiple values 
basket = ["apples","pears", "grapes", "mangoes", "bananas"]
print(basket)


# you can add items to your list
basket.append("figs")
print(basket)

# you can remove items from your list
basket.remove("apples")
print(basket)


# i can get the length of a list using len()
l= len(basket)
print("I have",l,"items in my list.")



# we can access one part of our list using a list index
#example: "mangoes is my third list item"
print(basket[2], "is my third list item")


# list indexes start at 0
first = basket[0]
print("My first item is", first)

# last index is -1
last = basket[-1]
print("My last item is",last)



# i can isolate parts of my list using list slicing

# EXAMPLE: isolate first half of list
l = len(basket)
l = int(l/2)
half = basket[0:l]
print(half)
