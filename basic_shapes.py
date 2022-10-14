from turtle import *

def ball(ball_color, ball_size):
    # This function draws a ball of any color and size

    pencolor(ball_color)
    fillcolor(ball_color)

    begin_fill()
    circle(ball_size)
    end_fill()


def box(box_color, box_size):
    pencolor(box_color)
    fillcolor(box_color)

    begin_fill()
    for i in range(4):
        forward(box_size)
        right(90)
    end_fill()
