from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

"""
move turtle with keypress
move cars
detect collision
detect when turtle reaches other side
create scoreboard
"""
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

        self.shape("turtle")
        self.penup()
        self.goStart()
        self.setheading(90) # VERTICAL

    def go_up(self):
        self.forward(MOVE_DISTANCE) #FORWARD!
    def go_down(self):
        self.backward(MOVE_DISTANCE)

    def finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False

    def goStart(self):
        self.goto(STARTING_POSITION)
