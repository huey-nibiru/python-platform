mynumbers = []
sum = 0

while True:
  #by default input is a string
  number = input("Enter 'quit' to quit or enter a number >>> ")
  if number == "quit":
    break
  number = int(number) # this turns it into a number
  mynumbers.append(number)
  sum += number
    
average = sum / len(mynumbers)
print("the average of these numbers is " + str(average))
  
  
  