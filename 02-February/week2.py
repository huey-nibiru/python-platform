"""
Project Name: PASSWORD MAKER
Concepts: string lib, conditions, loops
Homework: loop the program to make it run forever
"""

import random
import string
import time
import os

# INSTRUCTIONS
print("Create a password")
print("Password must be at least 8 letters")
print("Must include an uppercase letter")
print("Must include a lowercase letter")
print("Must include a number")
print("Must include a symbol")


# create a list that contains uppercase, lowercase, numbers, and symbols
digits = list(string.digits)
lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
symbols = list(string.punctuation)
length = 8
password = input("Please enter a password: ")

# check if password has digits
d = False

# check if password has uppercase
u = False 

# check if password has lowercase
l = False 

# check if password has symbols
s = False 


# verify each requirement PART 1
for letter in password:
  if letter in digits: 
    d = True
  if letter in lower: 
    l = True
  if letter in upper:
    u = True
  if letter in symbols:
    s = True


# verify each requirement PART 2
if (d == False) or (l == False) or (u == False) or (s == False) or len(password) < length:
  print("Invalid password")
else:
  print("Password created")
