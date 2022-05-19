 # LISTS REVIEW


# a list is a data type that holds multiple values 
fruits = ["apples","pears", "grapes", "mangoes", "bananas"]
print(fruits)


# you can add items to your list
fruits.append("figs")
print(fruits)

# you can remove items from your list
fruits.remove("apples")
print(fruits)


# i can get the length of a list using len()
l= len(fruits)
print("I have",l,"items in my list.")



# we can access one part of our list using a list index
#example: "mangoes is my third list item"
print(fruits[2], "is my third list item")


# list indexes start at 0
first = fruits[0]
print("My first item is", first)

# last index is -1
last = fruits[-1]
print("My last item is",last)



# i can isolate parts of my list using list slicing

# EXAMPLE: isolate first half of list
l = len(fruits)
l = int(l/2)
half = fruits[0:l]
print(half)
