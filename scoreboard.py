FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-50,250)
        self.score=0
        self.write_score()


    def write_score(self):
        self.clear()
        self.write(f"level : {self.score}", align="center",font=FONT)

    def increment_score(self):
        self.score+= 1
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over ", align="center", font=FONT)