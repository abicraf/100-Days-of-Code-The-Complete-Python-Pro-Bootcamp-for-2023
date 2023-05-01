from turtle import Turtle, Screen

UP = 20
DOWN = -20
UP_LIMIT = 300
DOWN_LIMIT = -300
STEP = 20
# P1_X_POS = 350
# P1_Y_POS = 0
# P2_X_POS = -350
# P2_Y_POS = 0

screen = Screen()
class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(x_pos, y_pos)

    def create_line(self):
        self.hideturtle()
        self.pensize(5)
        self.color("white")
        self.penup()
        self.setposition(0, DOWN_LIMIT)  # move starting point from the bottom
        while self.ycor() < UP_LIMIT:  # start drawing until it hit the up_limit
            self.pendown()
            self.setheading(90)  # Set Heading to North
            self.forward(STEP)  # start drawing every step
            self.penup()  # pen up for making space
            self.forward(STEP)  # moving without drawing.

    # def create_paddle(self, X_POS, Y_POS):
    #     self.shape("square")
    #     self.shapesize(5, 1)
    #     self.color("white")
    #     self.penup()
    #     self.goto(X_POS, Y_POS)

    def up(self):
        x_position = self.xcor()
        y_position = self.ycor()
        if y_position < UP_LIMIT:
            self.setposition(x_position, y_position + UP)

    def down(self):
        x_position = self.xcor()
        y_position = self.ycor()
        if y_position > DOWN_LIMIT:
            self.setposition(x_position, y_position + DOWN)