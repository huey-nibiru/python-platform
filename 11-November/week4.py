# DRAWING STAR FRACTALS WITH TURTLE


# REVIEW THE METHODS IN THE TURTLE DOCUMENTATION BEFORE AND AFTER EACH LESSON THAT INVOLVES TURTLE
# https://documentation.help/Python-3.7/turtle.html


# import turtle library to draw and create games using a pen object
import turtle

# allows us to use random numbers and random choice
import random


# create a pen object by assigning turtle.Turtle() to a variable
pen = turtle.Turtle()

# set the speed that the pen will draw
pen.speed(100)
  
# create a function to draw the fractal 
#       [explain what the parameters (n, x, d) are]
def draw(n, x, d):
    # loop for number of stars
    for i in range(n):
          
        # choosing random integers 
        # between 0 and 255
        # to generate random rgb values 
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
          
        # setting the outline 
        # and fill color
        pen.color(r,g,b)
        pen.fillcolor(r,g,b)
          
        # begins filling the star
        pen.begin_fill()
          
        # loop for drawing each star
        for j in range(5):
               
            pen.forward(5 * n-5 * i)
            pen.right(x)
            pen.forward(5 * n-5 * i)
            pen.right(72 - x)
              
        # colour filling complete
        pen.end_fill()
          
        # rotating for
        # the next star
        pen.right(d)
          
  
# setting the parameters
num_stars = 30    # number of stars
ext_angle = 144   # exterior angle of each star
degrees = 18    # angle of rotation for the spiral
  
# run the function 
draw(num_stars, ext_angle, degrees)