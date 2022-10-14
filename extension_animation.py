# This is an empty file for you to create your own animation!

from turtle import *
import time
from basic_shapes import ball, box
from helpers import no_delay, fly
import settings
from random import randint

def draw_animation(num_frames, sleeptime):
    # This function should animate a ball getting bigger and smaller

    ball_size = 100
    fly(-0,-100)

    r_val = randint(0,255)
    g_val = randint(0,255)
    b_val = randint(0,255)

   

    for i in range(num_frames):

        with no_delay():
            clear()

            for i in range(5):
                fly(randint(-300,300),randint(-300,300))
                r_val = randint(0,255)
                g_val = randint(0,255)
                b_val = randint(0,255)
                ball_color = (r_val,g_val,b_val)

                ball(ball_color,ball_size)
        

            if i < num_frames/2:
                ball_size += 1
            else:
                ball_size -= 1

            r_val += 10
            g_val += 10
            b_val += 10

            if r_val > 255:
                r_val = 0
            if g_val > 255:
                g_val = 0
            if b_val > 255:
                b_val = 0
            




        update()
        time.sleep(.1)




def main():
    screen = Screen()
    screen.setup(600,600)
    colormode(255)

    hideturtle()
    
    for i in range(3):
        draw_animation(settings.breathing_animation_num_frames, settings.breathing_animation_sleeptime)

    input("Press enter...")

main()


