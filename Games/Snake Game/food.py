from turtle import Turtle
import random
import constants as cst

class Food(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.spawn()

    def spawn(self):
        x_range = cst.GAME_FRAME_WIDTH//2-10
        y_range = cst.GAME_FRAME_HEIGHT//2-10
        x_pos = random.randint(-x_range, x_range) 
        y_pos = random.randint(-y_range, y_range)
        self.goto(x=x_pos, y=y_pos)
