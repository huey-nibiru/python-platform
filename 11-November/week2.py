# SPIRALS WITH TURTLE


# REVIEW THE METHODS IN THE TURTLE DOCUMENTATION BEFORE AND AFTER EACH LESSON THAT INVOLVES TURTLE
# https://documentation.help/Python-3.7/turtle.html


# import turtle library to draw and create games using a pen object
import turtle

# create a pen object by assigning turtle.Turtle() to a variable
pen = turtle.Turtle()

# you can adjust the shape of the pen object using the shape() method
pen.shape('turtle')

# set the speed that the pen will draw
pen.speed(100)

# you can adjust the screen settings by assigning turtle.Screen() to a variable
screen = turtle.Screen()

# change the screen color with bgcolor() method
screen.bgcolor("black")

# add as many colors as you would like to a color bank. The spiral will use these colors.
colorbank = ["silver", "gold"]

# find the amount of colors by calling the len() method on the colorbank
num_colors = len(colorbank)

# create the spiral size
size = 200

# set the spiral shape by using an amount of degrees
degrees = 82

# use a for loop to create a spiral with the size we specified
for i in range(size):

    # choose a new color for the pen each rotation
    pen.color(colorbank[i % num_colors] )
    
    # move the pen forward incrementally (explain this)
    pen.forward(i)

    # rotate the pen by the amount of degrees we specified
    pen.right(degrees)