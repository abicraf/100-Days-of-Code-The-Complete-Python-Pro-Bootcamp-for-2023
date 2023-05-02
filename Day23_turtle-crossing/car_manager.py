from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_X_POSITION = 280
FINISH_LINE_X = -280


## 2. Cars are randomly generated along the y-axis
# and will move from the right edge of the screen to the left edge.
class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_move = STARTING_MOVE_DISTANCE

    def generate_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(1, 2)

            # Car starting position
            new_car.color(random.choice(COLORS))  # randomly generated along the y-axis
            starting_y_position = random.randint(-280, 280)  # starting from the right edge
            new_car.setpos(STARTING_X_POSITION, starting_y_position)
            new_car.setheading(180)  # set turtle head to west.

            new_car.car_move = STARTING_MOVE_DISTANCE
            self.all_cars.append(new_car)

    def car_move_init(self):
        for car in self.all_cars:
            car.forward(self.car_move)

    def speed_up(self):
            self.car_move += MOVE_INCREMENT
