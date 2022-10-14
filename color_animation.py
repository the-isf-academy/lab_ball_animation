from turtle import *
import time
from basic_shapes import ball
from helpers import no_delay
import settings

def draw_animation(num_frames, sleeptime):
    # This function should animate a ball changing colors
    

    # Sets starting values for the RGB value of the ball color
    ball_color_r = 166
    ball_color_g = 166
    ball_color_b = 100

    for i in range(num_frames):

        with no_delay():
            clear()

            ball_color = (ball_color_r, ball_color_g, ball_color_b)   

            ball(ball_color,100)



        update()
        time.sleep(sleeptime)




def main():
    screen = Screen()
    screen.setup(600,600)

    hideturtle()

    colormode(255)
    bgcolor(239, 242, 187)

    
    
    for i in range(3):
        draw_animation(settings.color_animation_num_frames, settings.color_animation_sleeptime)

    input("Press enter...")

main()




