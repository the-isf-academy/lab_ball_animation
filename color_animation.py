from turtle import *
import time
from basic_shapes import ball, box
from helpers import no_delay

def draw_animation(num_frames, sleeptime):
    # This function animates a ball getting bigger and smaller
    
    ball_color_r = 166
    ball_color_g = 166
    ball_color_b = 166

    for i in range(num_frames):

        with no_delay():
            clear()

            ball_color = (ball_color_r, ball_color_g, ball_color_b)   

            ball(ball_color,100)

            ball_color_b += 5
            

            


        update()
        time.sleep(sleeptime)




def main():
    screen = Screen()
    screen.setup(600,600)

    colormode(255)
    bgcolor(239, 242, 187)

    hideturtle()
    
    for i in range(3):
        draw_animation(100, .05)

    input("Press enter...")

main()




