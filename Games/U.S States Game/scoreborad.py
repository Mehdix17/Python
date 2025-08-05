from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(275, 250)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score : {self.score}/50", align="center", font=("arial", 20, "normal"))

    def update_score(self):
        self.score += 1
        self.display_score()
