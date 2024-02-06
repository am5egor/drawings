from turtle import *

def draw(form, colour, size, count, forwards, degrees):
    i = 0
    shape(form)
    color(colour)
    pensize(size)
    while i < count:
        forward(forwards)
        left(degrees)
        i += 1

draw('turtle', 'green', 2, 4, 100, 90)
draw('turtle', 'yellow', 3, 3, 100, 120)
draw('turtle', 'red', 8, 360, 1, 1)

exitonclick()