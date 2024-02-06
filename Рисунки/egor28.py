from turtle import *

def draw(x, y):
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    for i in range(5):
        forward(70)
        left(144)
    end_fill()

speed(10)
color('blue')
x = -200
y = -200

for i in range(8):
    draw(x,y)
    x += 60
    y += 60

hideturtle()
exitonclick()