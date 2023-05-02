import time, random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

# Task 1. A turtle moves forwards when you press the "Up" key.
# It can only move forwards, not back, left or right.
screen.listen()
screen.onkey(player.move_turtle, "Up")

car_manager = CarManager()
scoreboard.update_level()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_cars()
    car_manager.car_move_init()

    ## 3. When the turtle hits the top edge of the screen,
    # it moves back to the original position and the player levels up. On the next level,
    # the car speed increases.
    if player.ycor() >= FINISH_LINE_Y:
        player.reset_position()
        #  the player levels up.
        scoreboard.update_level()
        #  On the next level, the car speed increases.
        car_manager.speed_up()

    ##4. When the turtle collides with a car, it's game over and everything stops.
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            collides = True
            scoreboard.game_over()
            game_is_on = False
            break


screen.exitonclick()





