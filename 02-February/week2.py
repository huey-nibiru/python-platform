#  PASSWORD MAKER

# these are modules ( toolsets ) 
import random
import string
import time
import os

# INSTRUCTIONS
print("Create a password")
print("Password must be at least 8 char")
print("Must include a number")
print("Must include a symbol")
print("Must include an uppercase char")


# create a list that contains uppercase, lowercase, numbers, and symbols
digits = list(string.digits)
lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
symbols = list(string.punctuation)
length = 8
password = input("Please enter a password: ")

# check the password length
if len(password) < length:
  print("Password too short")

# check if password has digits
d = False

# check if password has uppercase
u = False 

# check if password has symbols
s = False 


# verify each requirement PART 1
for letter in password:
  if letter in digits: 
    d = True
  if letter in upper:
    u = True
  if letter in symbols:
    s = True


# verify each requirement PART 2
if (d == False) or (u == False) or (s == False):
  print("Invalid password")
else:
  print("Password created")
