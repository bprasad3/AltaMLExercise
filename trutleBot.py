import time

import turtle
from turtle import Turtle

# Window Setup

window = turtle.Screen()

window.title("Turtle tracker")
turtle.bgcolor("darkolivegreen")
turtle.penup()

# File Selection (change as needed)
file = open("directions-3.txt", "r")
txt = file.readline()

# Turtle Setup
turtle.hideturtle()
myTurtle = Turtle()
myTurtle.speed(0)
myTurtle.color("black")
myTurtle.shape("turtle")
myTurtle.penup()
myTurtle.left(90)
myTurtle.goto(0, 0)
myTurtle.pendown()
time.sleep(1)
posList = set()
square_size = 1
turtle.color("red")

turtle.shape("square")
turtle.shapesize(square_size/10)

# Handle Movement
for f in txt:
    if f.upper() == 'F':
        myTurtle.forward(1)
        for inter in posList:
            if inter[0] == myTurtle.xcor() and inter[1] == myTurtle.ycor():
                turtle.setpos(inter)
                turtle.stamp()

        posList.add(myTurtle.position())
    elif f.upper() == 'R':
        myTurtle.right(90)
    elif f.upper() == 'L':
        myTurtle.left(90)




# Print Final Coordinate
myX = round(myTurtle.xcor())
myY = round(myTurtle.ycor())
turtle.goto(-200, 250)
turtle.write("Final Coords:  " + str(myX) + ", " + str(myY), font=("Arial", 30, "bold"))

# Exit onClick
turtle.exitonclick()

