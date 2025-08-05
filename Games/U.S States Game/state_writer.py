from turtle import Turtle

class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_state(self, state_name, x, y):
        self.goto(x, y)
        self.write(state_name, align='center', font=("arial", 10, "normal"))
    
    def game_over(self):
        self.goto(0,250)
        self.write("Game Over", align='center', font=("arial", 20, "normal"))
