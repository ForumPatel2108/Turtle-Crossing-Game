import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

Player1 = Player()
Car = CarManager()
score = Scoreboard()


screen.listen()
screen.onkeypress(Player1.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    Car.create_car()
    Car.move_car()


#Detect successfull crossing
    if Player1.reached_finish_line():
        Player1.go_to_start()
        Car.level_up()
        score.score_update()


#Detect collision
    for car in Car.all_cars:
        if car.distance(Player1) < 20:
            game_is_on = False
            score.game_over()
            






screen.exitonclick()
