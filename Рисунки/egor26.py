from turtle import *

def paint():
    size = 10
    for i in range(7):
        circle(size)
        size += 10  


color('red')
for i in range(4):
    left(90)
    paint()
hideturtle()
exitonclick()