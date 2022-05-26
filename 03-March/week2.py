"""
Project Name: IS THIS WALDO?
Concepts: random lib, variables, lists, functions, loops
Homework: test out the program with different names, jobs, and countries
"""


# conditions are decisions that evaluate
# to True or False
import time

name = "Waldo"
job = "Programmer"
country = "America"


print
# check if name is jimmy
if (name == "Waldo"):
  print("This is Waldo.")
else:
  print("This is not Waldo. This is " + name + ".")

  
# check if job is programmer
if (job == "Programmer" ):
  print("He is a " + job)
else:
  print("He is not a programmer. He is a " + job + ".")


  
  
# comparison operators compare value 
# they are: (>, <, ==, >= , <=)
# logical operators check inclusion/exclusion 
# they are: (AND, OR, NOT)
# we can save conditions in a variable
is_american = (country == "America") 
if is_american:
  print("Waldo is American")
else:
  print(name + " is not American. He is from", country, ".")













  
  

















