from turtle import Turtle
import constants as cst

class ScoreBorad(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.hideturtle()
        self.up()
        self.color("white")
        self.goto(x=0, y=cst.SCREEN_HEIGHT//2*0.85)
        self.display_scoreboard()  
    
    def display_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}      High score = {self.high_score}", move=False, align=cst.ALIGNEMENT, font=cst.FONT)

    def update_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", 'w') as data:
                data.write(str(self.high_score))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        self.display_scoreboard()

    def reset(self):
        self.update_scoreboard()
        self.score = 0
        self.display_scoreboard()
