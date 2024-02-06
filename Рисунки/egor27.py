from turtle import *

def draw(colour, size):
    color(colour)
    begin_fill()
    for i in range(4):
        forward(size)
        left(90)
    end_fill()

penup()
goto(-50,-50)
pendown()

draw('black', 200)
draw('white', 150)
draw('lavender', 100)
draw('black', 50)

hideturtle()
exitonclick()