import turtle

# turtle library is used to draw 

# first make a pen object
pen = turtle.Turtle()

pen.width(3)
pen.speed(100)


# lift the pen up
pen.penup()

# go to a coordinate
pen.goto(0,-50)

# lower the pen
pen.pendown()

# draw the head
pen.color("yellow")
pen.begin_fill()
pen.circle(100)
pen.end_fill()
pen.color("black")


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


# make the smiley mouth
pen.penup()
pen.goto(-15,0)
pen.pendown()
pen.right(90)
pen.begin_fill()
pen.circle(15,180)
pen.end_fill()
pen.hideturtle()









