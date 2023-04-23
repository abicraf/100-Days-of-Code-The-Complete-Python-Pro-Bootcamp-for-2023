from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.pencolor("red")
        self.write(f"Points = {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.pencolor("white")
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def write_score(self):
        self.score += 1
        self.clear()
        self.write(f"Points = {self.score}", False, align=ALIGNMENT, font=FONT)
