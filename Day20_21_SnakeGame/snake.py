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
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        a_snake = Turtle(shape="square")
        a_snake.penup()
        a_snake.color("white")
        a_snake.setposition(position)
        a_snake.speed('slowest')
        self.snake.append(a_snake)

    def add_tail(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for item in range(len(self.snake) - 1, 0, -1):
            x = self.snake[item - 1].xcor()
            y = self.snake[item - 1].ycor()
            self.snake[item].setposition(x, y)
        self.head.forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)  # set heading to North

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)  # set heading to South

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)  # set heading to East

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)  # set heading to West
