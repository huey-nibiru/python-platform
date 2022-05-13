# create a list that will store the numbers that are being averaged
numbers = []


# this while loop will let us keep adding new numbers into the list of numbers
while True:
  
  # let the user input the number they want to average 
  number = input("Enter 'quit' to quit or enter a number >>> ")
  
  # if the user enters the word 'quit' the loop will stop and the average will show
  if number == "quit":
    break
  
  # when the user enters a number, we will convert it from string to integer
  # we then add each number to the list of numbers
  else:
    
    # if the user enters any letters, the computer will tell us to enter only numbers
    try:
      number = int(number) 
      numbers.append(number)
    except:
      print("Please enter a number only.\n")


# create the average by taking the sum of the list and divide by length of the list
average = sum(numbers) / len(numbers)

# display the outcome
print("\nNumbers:", numbers)
print("Average:", average)