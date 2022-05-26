"""
Project Name: GENERAL QUIZ
Concepts: conditions, variables, input
Homework: add more quiz questions
"""

print('Welcome to AskPython Quiz')

score=0
total_questions=3
 

answer=input('Question 1: What is the capital of New York?')
if answer.lower()=='albany':
    score += 1
    print('correct')
else:
    print('Wrong Answer :(')


answer=input('Question 2: What color is the sky? ')
if answer.lower()=='blue':
    score += 1
    print('correct')
else:
    print('Wrong Answer :(')

answer=input('Question 3: What continent is Turkmenistan in?')
if answer.lower()=='asia':
    score += 1
    print('correct')
else:
    print('Wrong Answer :(')
 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')
Ou