"""
Project Name: CRAZY STAR
Concepts: turtle, methods, loops, operators
Homework: change the color of the star
"""


import turtle  
# Creating turtle  
t = turtle.Turtle()  
s = turtle.Screen()  
s.bgcolor("black")  
t.pencolor("white")  
  
# set the steps and angle at 0
steps = 0  
angle = 0  

# set the pen origin
t.speed(0)  
t.penup()  
t.goto(0,200)  
t.pendown()  


# draw the star
while(True):  
    t.forward(steps)  
    t.right(angle)  
    steps+=3  
    angle+=1  
    if angle == 210:  
        break  
    t.hideturtle()  
  
turtle.done()  