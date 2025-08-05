import constants as cst
from turtle import Turtle

class ScreenDrawer(Turtle):

    def __init__(self):
        super().__init__()

        self.speed(0) # Fastest speed
        self.color("white")
        self.penup()

        # Move to the top-left corner for drawing the border
        self.goto(-cst.GAME_FRAME_WIDTH//2, cst.GAME_FRAME_HEIGHT//2)
        self.pendown()
        self.pensize(2)

        # Draw the border
        for _ in range(2):
            self.forward(cst.GAME_FRAME_WIDTH)  # Move across the width
            self.right(90)
            self.forward(cst.GAME_FRAME_HEIGHT)  # Move across the height
            self.right(90)

        self.hideturtle()  # Hide the turtle after drawing the border
