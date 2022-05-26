"""
Project Name: CALCULATOR
Concepts: variables, loops, functions, parameters, operators
Homework: add an exponent option
"""



# allows us to clear the screen 
import os

# allows us to pause the screen
import time


# create a function that lets the computer clear screen after an amount of seconds (discuss parameters)
def clr(seconds):
  # let the computer pause for an amount of seconds
  time.sleep(seconds)
  # clear the screen
  os.system("clear")  


# create a function that returns the sum of two parameters
def add(x,y):  
  return x + y 
 

# create a function that returns the difference of two parameters
def subtract(x,y):
  return x - y


# create a function that returns the quotient of two parameters
def divide(x,y):
  return x / y


# create a function that returns the product of two parameters
def multiply(x,y):
  return x * y
   

# create the menu with options
def menu():
  clr(1)
  print("1 -- ADD") 
  print("2 -- SUBTRACT")
  print("3 -- DIVIDE")
  print("4 -- MULTIPLY")
  print("5 -- QUIT")
  
  # create an integer input to choose an operation
  choice = int(input("Choose an operation >>>"))

  # use a for loop to cycle through options
  for i in range(1,6):
    
    # only allow integer input
    try:
      number1 = int(input("Number 1 >>> ")) 
      number2 = int(input("Number 2 >>> "))
    
    # restart menu if letters are input
    except:
      print("invalid input")
      menu()
    
    # addition
    if choice == 1:
      print("%d + %d = %d" % (number1, number2, add(number1,number2)))
  
    # subtraction
    elif choice == 2:
      print("%d - %d = %d" % (number1, number2, subtract(number1,number2)))
  
    # division
    elif choice == 3: 
      print("%d / %d = %d" % (number1, number2, divide(number1,number2)))
    
    # multiplication
    elif choice == 4:
      print("%d * %d = %d" % (number1, number2, multiply(number1,number2)))
   
  # exit(0) quits all processes
    elif choice == 5:
      print("Bye")
      exit(0) 
    
    # invalid input
    else:
      print("NOT A VALID CHOICE")
      clr(1) # clears he screen for one second
      menu() # returns the menu to try again


# run the menu function to begin the program
menu() 


  
'''
CONCEPTS
  - libraries
  - functions & parameters
  - parameters
  - variables
  - return statements
  - built in functions
  - try/except
  - if statements


HOMEWORK
  - 
'''