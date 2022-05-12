# these are modules ( toolsets ) 
import random
import string
import time
import os

print("Create a password")
print("Password must be at least 8 char")
print("Must include a number")
print("Must include a symbol")
print("Must include an uppercase char")

digits = list(string.digits)
lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
symbols = list(string.punctuation)
length = 8
password = input("Please enter a password: ")

if len(password) < length:
  print("Password too short")

d = False #check if password has digits
u = False #check if password has uppercase
s = False #check if password has symbols

for letter in password:
  if (letter in digits): 
    d = True
  if (letter in upper):
    u = True
  if (letter in symbols):
    s = True

if d == False or u == False or s == False:
  print("Invalid password")
else:
  print("Password created")




  
  


























