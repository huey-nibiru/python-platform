# DRAWING POLYGONS WITH TURTLE


# REVIEW THE METHODS IN THE TURTLE DOCUMENTATION BEFORE AND AFTER EACH LESSON THAT INVOLVES TURTLE
# https://documentation.help/Python-3.7/turtle.html


# import turtle library to draw and create games using a pen object
import turtle

# import time to pause screen between each drawing
import time

# set a variable for the reset time
reset_time = 2

# create a pen object by assigning turtle.Turtle() to a variable
pen = turtle.Turtle()

# go to the middle of the screen
pen.goto(0,0)
 

# [discuss the logic behind how each shape is drawn]


# draw a square
for i in range(4):
    pen.forward(50)
    pen.right(90)

# reset the screen after the amount of reset time
time.sleep(reset_time)
pen.reset()
 

# draw a star
for i in range(5):
    pen.right(144)
    pen.forward(100)
    
# reset the screen after the amount of reset time
time.sleep(reset_time)
pen.reset()


# draw a hexagon
for i in range(6):
    pen.forward(70)
    pen.right(60)
     
# reset the screen after the amount of reset time
time.sleep(reset_time)
pen.reset()