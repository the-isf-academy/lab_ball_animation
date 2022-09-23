from turtle import *
import time
from basic_shapes import ball
from movement import no_delay

def draw_animation(num_frames, sleeptime):
    # This function animates a ball getting bigger and smaller

    for i in range(num_frames):

        with no_delay():
            clear()

            # YOUR CODE GOES HERE#
            if i  < 50:
                ball_size = ball_size + 1
            else:
                ball_size = ball_size - 1


            ball('purple',ball_size)


        screen.update()
        time.sleep(sleeptime)




if __name__ == '__main__':
    screen = Screen()
    screen.setup(600,600)

    hideturtle()
    
    for i in range(3):
        draw_animation(100, .005)

    input("Press enter...")




