STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.start_position()


    def start_position(self):
        self.goto(0,-280)

    def move_player(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)
        print(new_y)

