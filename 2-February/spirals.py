# the turtle library lets us draw
# we import it to use the tools we want
import turtle



# we need to create a pen
pen = turtle.Turtle()

# we can change the screen settings
screen = turtle.Screen()
screen.bgcolor("black")

#change the pen color
pen.color("gold")

#change the pen speed
pen.speed(100)

# declare spiral size
size = 200

# declare spiral shape
shape = 73


# create the spiral with a loop
for i in range(size):
  pen.forward(i)
  pen.right(shape)






