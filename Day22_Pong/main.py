from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

P1_X_POS = 350
P1_Y_POS = 0
P2_X_POS = -350
P2_Y_POS = 0
LINE_X_POS = 0
LINE_Y_POS = 0
game_on = True

# define Screen
screen = Screen()
screen.setup(width=1000, height=800)
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor("black")
screen.title("Pong")

#score = Score()

screen.tracer(0)

# draw the middle-line
line = Paddle(LINE_X_POS, LINE_Y_POS)
line.create_line()
ball = Ball()
score = Score()


# draw the Paddles
paddle1 = Paddle(P1_X_POS, P1_Y_POS)
# paddle1.create_paddle(P1_X_POS, P1_Y_POS)
paddle2 = Paddle(P2_X_POS, P2_Y_POS)
# paddle2.create_paddle(P2_X_POS, P2_Y_POS)



# define Hotkey to move Paddles
screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "e")
screen.onkey(paddle2.down, "d")
collision = False

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    # create ball.py to let the ball run
    ball.move()
    # detect collision with wall and bounce
    if (ball.ycor() >= 220) or (ball.ycor()<=-220):
        ball.bounce_y()
    if ((ball.distance(paddle1) < 50) and (ball.xcor() > P1_X_POS)) or ((ball.distance(paddle2) < 50) and (ball.xcor() < P2_X_POS)):
        ball.bounce_x()
    elif ball.xcor() > P1_X_POS + 50 and ball.xcor() > 0:
        #if the right paddle missed the ball, left paddle add one point.
        ball.reset_ball()
        score.l_add_points()
    elif ball.xcor() < P2_X_POS - 50 and ball.xcor() < 0:
        # if the left paddle missed the ball, right paddle add one point.
        ball.reset_ball()
        score.r_add_points()




screen.exitonclick()


# detect the collision of ball and two paddles for the score.
# detect with paddles misses
# create score.py to get and present the score