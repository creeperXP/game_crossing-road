from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle() # why is this needed
        self.penup()
        self.level = 1
        self.goto(-280, 250)
        self.updateScoreboard()

    # use these 2 combinations when updating
    def increaseLevel(self):
        self.level +=1
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align = "left", font = FONT)

    def gameover(self):
        self.goto(0,0) # center
        self.write(f"GAME OVER", align = "center", font = FONT)


