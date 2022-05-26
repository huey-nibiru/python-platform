"""
Project Name:  FIREWORKS
Concepts:  turtle, random lib, loops
Homework: contain the code that draws the fireworks inside a function, then call the function in the loop instead
"""
import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(1000)
t.color("white")


for i in range(20):
  x = random.randint(-250, 250)
  y = random.randint(-250,250)
  t.penup()
  t.goto(x,y)
  t.pendown()

  size = random.randint(2, 8)
  for i in range(5):
    t.forward(size)
    t.backward(size)
    t.left(72)


for i in range(10):
  x = random.randint(-250, 250)
  y = random.randint(-250,250)
  t.penup()
  t.goto(x,y)
  t.pendown()

  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  t.color(r,g,b)

  size = random.randint(30, 200)
  for i in range(36):
    t.forward(size)
    t.backward(size)
    t.left(10)
