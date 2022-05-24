# TEST GRADE AVERAGES



# return the leter grades of each student
def grade_converter(grade): 
  if grade >= 90 and grade <= 100:
    return "A"
  elif grade >= 80 and grade <= 89:
    return "B"
  elif grade >= 70 and grade <= 79:
    return "C"
  elif grade >= 65 and grade <= 69:
    return "D"
  else: 
    return "F"

# return the average score 
def averageScore(testScores):
  mysum = 0 # set the variable to 0 so it doesnt interfere
  for eachScore in testScores:
    mysum += eachScore
  average = mysum/len(testScores)
  print("Your Test average is a " + grade_converter(average))
  
  
# holds the list of test grades
tests = [ ]

# create a counter for each test: *test #1*
x = 1

print("It is time to grade the exams")
numTests = int(input("How many test Scores? "))
for i in range(numTests):
    
    # input test scores
    y = int(input("Test score " + str(x) + ":" )) 
    tests.append(y)
    print (str(grade_converter(y))
    
    # update counter
    x+=1
    averageScore(tests) 