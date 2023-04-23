from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.screensize(500, 500)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game!")

game_on = True
screen.tracer(0)

# create a snake
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

screen.listen()

while game_on:
    screen.update()
    time.sleep(0.1)

    # move one step
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_tail()
        scoreboard.write_score()

    # detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_on = False
        scoreboard.game_over()

    # detect collision with tail
    # if head hit the tail, then game over.
    # using Slicing to modify it.

    # for tail in snake.snake:
    # if tail == snake.head:
    #     pass
    for tail in snake.snake[1:]:  # slicing.
        if snake.head.distance(tail) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
