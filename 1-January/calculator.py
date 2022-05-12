import time
import os 

# time and os are modules/libraries 
# modules/libaries are toolsets we use to do specific functions

def clr(seconds):
  time.sleep(seconds)# computer pauses for an amount of seconds
  os.system("clear") # computer clears screen

def add(x,y):  # parameters go inside the parentheses 
  return x + y 
 
def subtract(x,y):
  return x - y

def divide(x,y):
  return x / y

def multiply(x,y):
  return x * y
   
def menu():
  clr(1)
  print("1 -- ADD") 
  print("2 -- SUBTRACT")
  print("3 -- DIVIDE")
  print("4 -- MULTIPLY")
  print("5 -- EXIT")
  
  # one equal sign assigns a value to a variable
  # two equal signs checks for a value
  
  
  choice = input("Choose an operation >>>")
  # by default every input is a string
  # we have to put int() around the input
  # to turn it into a number

  
  if choice == '1':
    try:
      number1 = int(input("Number 1 >>> ")) 
      number2 = int(input("Number 2 >>> "))
      print("%d + %d = %d" % (number1, number2, add(number1,number2)))
    except:
      print("invalid input")
      menu()
  
  
  elif choice == '2':
    try:
      number1 = int(input("Number 1 >>> ")) 
      number2 = int(input("Number 2 >>> "))
      print("%d - %d = %d" % (number1, number2, subtract(number1,number2)))
    except:
      print("invalud input")
      menu()
    
    
  elif choice == '3':
    try:
      number1 = int(input("Number 1 >>> ")) 
      number2 = int(input("Number 2 >>> "))
      print("%d / %d = %d" % (number1, number2, divide(number1,number2)))
    except:
      print("invalid Input")
      menu()
      
      
  elif choice == '4':
    try:
      number1 = int(input("Number 1 >>> ")) 
      number2 = int(input("Number 2 >>> "))
      print("%d * %d = %d" % (number1, number2, multiply(number1,number2)))
    except ValueError:
      print("invalid input")
      menu()
      
      
  elif choice == '5':
    print("BYE") ; exit(0) # exit(0) means end the program. stop all.
  
  else:
    print("NOT A VALID CHOICE")
    clr(1) # clears he screen for one second
    menu() # returns the menu to try again

menu() # starts the whole thing
# we need to call the function outisde of everything
# this call will be all the way to the left
  
  
# we use a try except when we want t 
  
  
  
  
  
  




