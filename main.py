import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# create screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# important to get keypresses
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update() # IMPORTANT

    # create cars
    car_manager.createcar()
    car_manager.movecar()

    # detect collision with car
    for car in car_manager.allcars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameover()

    # if player reaches end
    if player.finish():
        player.goStart()
        scoreboard.increaseLevel()
screen.exitonclick() # IMPORTANT!
