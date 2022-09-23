from turtle import *

def ball(ball_color, ball_size):
    # This function draws a ball of any color and size

    pencolor(ball_color)
    fillcolor(ball_color)

    begin_fill()
    circle(ball_size)
    end_fill()

