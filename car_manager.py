import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

from turtle import Turtle


class CarManager:
    def __init__(self):
        self.car_list = []
        self.constant_pace=5






    def create_car(self):
        key=random.randint(1,6)
        if key==1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(280, random.randint(-280, 280))
            self.car_list.append(new_car)

    def move_car(self):
        for carr in self.car_list:

            new_position_x= carr.xcor()-self.constant_pace
            carr.goto(new_position_x,carr.ycor())

    def move_encriment(self):
        self.constant_pace+=10

