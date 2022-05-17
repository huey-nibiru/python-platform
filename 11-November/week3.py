# DRAWING A SMILEY FACE WITH TURTLE


# REVIEW THE METHODS IN THE TURTLE DOCUMENTATION BEFORE AND AFTER EACH LESSON THAT INVOLVES TURTLE
# https://documentation.help/Python-3.7/turtle.html


# import turtle library to draw and create games using a pen object
import turtle

# create a pen object by assigning turtle.Turtle() to a variable
pen = turtle.Turtle()

# adjust the width of the pen 
pen.width(3)

# set the speed that the pen will draw
pen.speed(100)

# lift the pen up so it doesnt draw
pen.penup()

# go to a coordinate on the screen
pen.goto(0,0)

# lower the pen to draw
pen.pendown()


# draw the head
pen.color("yellow") # select the color
pen.begin_fill()    # set the pen to fill in a shape with the colors selected
pen.circle(100)     # create the circle
pen.end_fill()      # end the fill sequence
pen.color("black")  # reset color to black


# make the left eye
pen.penup()
pen.goto(-50,60)
pen.pendown()
pen.begin_fill()
pen.circle(15)
pen.end_fill()


# make the right eye
pen.penup()
pen.goto(50,60)
pen.pendown()
pen.begin_fill()
pen.circle(15)
pen.end_fill()


# make the mouth
pen.penup()
pen.goto(-15,0)
pen.pendown()
pen.right(90)
pen.begin_fill()
pen.circle(15,180)
pen.end_fill()
pen.hideturtle() # hide the pen


