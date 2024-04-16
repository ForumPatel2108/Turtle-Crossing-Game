from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250,250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level : {self.level}",FONT, align="center")


    def score_update(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("Game over", FONT,align="center")

        


