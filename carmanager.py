
import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.allcars = [] # ALWAYS FOR SELF
        self.carspeed = STARTING_MOVE_DISTANCE

    def createcar(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1: # chance to spawn a new "car"
            newcar = Turtle("square")

            newcar.shapesize(stretch_wid=1,stretch_len=2) # change dimensions
            newcar.penup() # can move
            newcar.color(random.choice(COLORS))
            randomy = random.randint(-250,250)
            newcar.goto(300, randomy)
            self.allcars.append(newcar) # US ETHIS

    def movecar(self):
        for car in self.allcars: # ALWAYS SELF
            car.backward(self.carspeed) # BACKWARD

    def levelUp(self):
        self.carspeed += MOVE_INCREMENT

