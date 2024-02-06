from turtle import *

def draw(colour, radius, x, y):
    penup()
    goto(x, y)
    pendown()
    color(colour)
    begin_fill()
    circle(radius)
    end_fill()


draw('yellow', 29, 40,100)
draw('green', 43, 84,-80)
draw('red', 83, -89,1)

exitonclick()
hideturtle()