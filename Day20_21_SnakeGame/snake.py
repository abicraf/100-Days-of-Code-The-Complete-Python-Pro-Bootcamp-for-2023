from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            a_snake = Turtle(shape="square")
            a_snake.penup()
            a_snake.color("white")
            a_snake.setposition(position)
            a_snake.speed('slowest')
            self.snake.append(a_snake)

    def move(self):
        for item in range(len(self.snake) - 1, 0, -1):
            x = self.snake[item - 1].xcor()
            y = self.snake[item - 1].ycor()
            self.snake[item].setposition(x, y)
        self.snake[0].forward(MOVING_DISTANCE)

    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP) # set heading to North
    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN) # set heading to South
    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT) # set heading to East
    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT) # set heading to West
