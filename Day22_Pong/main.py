from turtle import Screen, Turtle
from paddle import Paddle
#from score import Score

P1_X_POS = 350
P1_Y_POS = 0
P2_X_POS = -350
P2_Y_POS = 0
LINE_X_POS = 0
LINE_Y_POS = 0
game_on = True

# define Screen
screen = Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor("black")
screen.title("Pong")

#score = Score()

screen.tracer(0)

# draw the middle-line
line = Paddle(LINE_X_POS, LINE_Y_POS)
line.create_line()


# draw the Paddles
paddle1 = Paddle(P1_X_POS, P1_Y_POS)
# paddle1.create_paddle(P1_X_POS, P1_Y_POS)
paddle2 = Paddle(P2_X_POS, P2_Y_POS)
# paddle2.create_paddle(P2_X_POS, P2_Y_POS)



# define Hotkey to move Paddles
screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

while game_on:
    screen.update()

screen.exitonclick()

# create ball.py to let the ball run, define the running scope
# detect collision with wall and bounce

# detect the collision of ball and two paddles for the score.
# detect with paddles misses
# create score.py to get and present the score