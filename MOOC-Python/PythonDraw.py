# PythonDraw.py
import turtle

turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80 / 2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2 / 3)
turtle.done()

## improve code
from turtle import *

setup(850, 350)
penup()
fd(-250)
pendown()
pensize(25)
pencolor("purple")
seth(-40)
for i in range(5):
    circle(40, 80)
    circle(-40, 80)
circle(40, 80 / 2)
fd(40)
circle(16, 180)
fd(40 * 2 / 3)
done()

# import a as b code
import turtle as t

t.setup(650, 350, 200, 200)
t.penup()
t.fd(-250)
t.pendown()
t.pensize(25)
t.pencolor("purple")
t.seth(-40)
for i in range(4):
    t.circle(40, 80)
    t.circle(-40, 80)
t.circle(40, 80 / 2)
t.fd(40)
t.circle(16, 180)
t.fd(40 * 2 / 3)
t.done()
