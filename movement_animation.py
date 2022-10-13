from turtle import *
import time
from basic_shapes import ball
from movement import no_delay

def draw_animation(num_frames, sleeptime):
    # This function animates a ball moving up and down

    y_position = 0

    for i in range(num_frames):

        with no_delay():
            clear()

            if i  < 50:
                y_position = y_position - 5
            else:
                y_position = y_position + 5

            goto (0,y_position)

            ball('purple',60)


        update()
        time.sleep(sleeptime)




def main():
    screen = Screen()
    screen.setup(600,600)
    
    hideturtle()
    
    for i in range(3):
        draw_animation(100, .005)

    input("Press enter...")

main()