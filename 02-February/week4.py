# TEST GRADE AVERAGES

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


def averageScore(testScores):
  mysum = 0 # set the variable to 0 so it doesnt interfere
  for eachScore in testScores:
    mysum += eachScore
  average = mysum/len(testScores)
  print("Your Test average is a " + grade_converter(average))
  
  

tests = [ ]
x = 1
print("It is time to grade the exams")
numTests = int(input("How many test Scores? "))
for i in range(numTests):
  y = int(input("Test score " + str(x) + ":" )) 
  tests.append(y)
  print str(grade_converter(y)) 
  x+=1
averageScore(tests) 