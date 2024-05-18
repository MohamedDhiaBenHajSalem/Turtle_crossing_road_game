import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player=Player()


screen.onkey(fun=player.move_player,key="Up")
car=CarManager()
score=Scoreboard()




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()




    if player.ycor()>280:
        player.start_position()
        car.move_encriment()
        score.increment_score()

    for carr in car.car_list :

        if player.distance(carr)<20:
            game_is_on=False
            score.game_over()






screen.exitonclick()