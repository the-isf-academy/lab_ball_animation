from turtle import *
import time
from basic_shapes import ball
from helpers import no_delay, fly
import settings

def draw_animation(num_frames, sleeptime):
    # This function should animate a ball getting bigger and smaller

    ball_size = 100
    fly(-0,-100)

    for i in range(num_frames):

        with no_delay():
            clear()

            ball('purple',ball_size)

     


        update()
        time.sleep(sleeptime)




def main():
    screen = Screen()
    screen.setup(600,600)

    hideturtle()
    
    for i in range(3):
        draw_animation(settings.breathing_animation_num_frames, settings.breathing_animation_sleeptime)

    input("Press enter...")

main()


