from turtle import Screen, Turtle
import random

screen = Screen()
screen.screensize(250, 250)
user_guess = screen.textinput("Turtle Racing Guess", "Guess who's the winner?").lower()

game_continue = True
rainbow_color = ["green", "purple", "red", "blue", "black", "orange", "yellow"]
all_turtle = []
y = [50, -50, 100, -150, 0, 150, -100]
random_distance = [0, 5, 10, 15, 20]

for item in range(0,7):
    a_turtle = Turtle(shape="turtle")
    a_turtle.penup()
    a_turtle.color(rainbow_color[item])
    a_turtle.setposition(-230, y[item])
    a_turtle.speed('fastest')
    all_turtle.append(a_turtle)
    #print(a_turtle)

while game_continue:
    for item in range(0, 7):
        all_turtle[item].forward(random.choice(random_distance))
        #print(all_turtle[item].position())
        if all_turtle[item].xcor() >= 230:
            print(f"Turtle {all_turtle[item].pencolor()} is the winner.")
            print(f"Your bet is {user_guess}")
            if user_guess == all_turtle[item].pencolor():
                print("You Win!!!")
            else:
                print("Wrong bet.")
            game_continue = False
            break

# def forward():
#     tim.forward(50)
#
# def backward():
#     tim.backward(50)
# def counter_clockwise():
#     #screen.mode("standard")
#     tim.left(10)

# def clockwise():
#     #screen.mode("logo")
#     tim.right(10)
#
# def clear_screen():
#     tim.home()
#     tim.clear()


# screen.onkey(forward, "W")
# screen.onkey(backward, "S")
# screen.onkey(counter_clockwise, "A")
# screen.onkey(clockwise, "D")
# screen.onkey(clear_screen, "C")


#screen.listen()

screen.exitonclick()