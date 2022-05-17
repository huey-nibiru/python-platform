# USING LISTS (with fruit example)

# a list is a data type that holds multiple values 
print("1. Create a list of basket.")
basket = ["apples","pears", "grapes", "mangoes", "bananas"]
print(basket,"\n")


# you can add items to your list with append()
print("2. Add a new fruit to the basket.")
basket.append("figs")
print(basket,"\n")


# you can remove items from your list with remove()
print("3. Remove a fruit from the basket.")
basket.remove('apples')
print(basket,"\n")


# i can get the length of a list using len()
print("4. Print total fruit.")
amount = len(basket)
print("I have",amount,"fruits in my basket.", "\n")


print("5. Print the third fruit in your basket.")
print(basket[2], "is my third list item", "\n")

# access an element of the list using a list index
# list indexes start at 0
first = basket[0]

# last index is -1
last = basket[-1]

print("6. Print the first & last fruit in your basket.")
print("My first fruit is", first)
print("My last fruit is",last,"\n")


# [review what list slicing is]
print("7. Print the first half of fruits in your basket.")
all = len(basket) +1
middle = all//2
first_half = basket[ :middle]
print("My first half of basket are",first_half)
