from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0

    def update_level(self):
        self.level += 1
        self.clear()
        self.goto(-280, 200)
        self.write(f"Level: {self.level}", align = "left", font = FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align = "center", font = FONT)