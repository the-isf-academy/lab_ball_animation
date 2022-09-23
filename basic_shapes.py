from turtle import *

def ball(ball_color, ball_size):
    # This function draws a ball of any color and size

    pencolor(ball_color)
    fillcolor(ball_color)

    begin_fill()
    circle(ball_size)
    end_fill()

def box(box_color, box_size):
    # This function draws a box of any color and size

    fillcolor(box_color)

    begin_fill()
    for i in range(4):
        forward(box_size)
        left(90)

    end_fill()