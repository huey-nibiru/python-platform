# allows us to use random numbers and random choice
import random

# create a variable that holds information for a person. [review variables with class]
name = "Yousef"
age = 25

# use string concatenation to combine words with the values our variables have
print("my name is " + name)

# in string concatenation, integers must have str() around them 
print("I am " + str(age) + " years old")


# create a list of favorite foods. Choose 3 - 10 foods
favFoods = ["chicken", "chocolate", "Cheese burgers"]

# randomly select a food from the list of foods
randomFood = random.choice(favFoods)

# output the result
print("One of my favorite foods is " + randomFood)
