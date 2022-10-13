from turtle import *
import time
from basic_shapes import ball, box
from movement import no_delay

def draw_animation(num_frames, sleeptime):
    # This function animates a ball getting bigger and smaller
    for i in range(num_frames):

        with no_delay():
            clear()

            # YOUR CODE GOES HERE#
            if i%2 == 0:
                ball('light blue',100)

            else:
                box('pink',200)

            


        update()
        time.sleep(sleeptime)




def main():
    screen = Screen()
    screen.setup(600,600)
    bgcolor('dark blue')

    hideturtle()
    
    for i in range(3):
        draw_animation(100, .5)

    input("Press enter...")

main()




