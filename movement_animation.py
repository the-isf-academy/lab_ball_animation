from turtle import *
import time
from basic_shapes import ball
from helpers import no_delay, fly
import settings

def draw_animation(num_frames, sleeptime):
    # This function should animatee a ball moving up and down


    # sets the starting position of the ball
    x_position = 0
    y_position = 0

    for i in range(num_frames):

        with no_delay():
            clear()

            fly(x_position, y_position)

            ball('light blue',60)


        update()
        time.sleep(sleeptime)




def main():
    screen = Screen()
    screen.setup(600,600)
    
    hideturtle()
    
    for i in range(3):
        draw_animation(settings.movement_animation_num_frames, settings.movement_animation_sleeptime)

    input("Press enter...")

main()