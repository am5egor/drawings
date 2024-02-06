from turtle import *

# квадрат
def square(colour_border, colour):
    # colour_border-граница, colour-заливка.
    color(colour_border, colour)
    begin_fill()
    for i in range(4):
        forward(50)
        left(90)
    end_fill()
    # для отрисовки квадрата в другом месте.
    forward(50)

# отрисовка линий из квадратов
def line(x,y, n,m):
    penup()
    goto(x,y)
    pendown()
    # для чередования цветов квадратов(чётное или нечётное)
    for j in range(n,m): 
        if j % 2 == 0:
            square('black', 'black')
        else:
            square('black', 'white')

x = -200
y = 150
speed(100)

# отрисовка шахмотной доски
for h in range(8):
    # для чередования цветов
    if h % 2 == 0:
        line(x,y, 0,8)
    else:
        line(x,y, 1,9)
    y -= 50

hideturtle()
exitonclick()