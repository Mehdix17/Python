import constants as cst
import time
from turtle import Turtle

class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for postion in cst.STARTING_POSTION:
            new_segment = Turtle("square")
            new_segment.color("chartreuse")
            new_segment.up()
            new_segment.goto(postion)
            self.body.append(new_segment)

    def reset(self):
        for segment in self.body:
            segment.goto(cst.SCREEN_WIDTH*2, cst.SCREEN_HEIGHT*2)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

    def move(self):
        time.sleep(0.02)
        
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].goto(self.body[i-1].pos())
        
        self.head.forward(cst.MOVE_DISTANCE)

        # check if snake hits a border

        if abs(self.head.xcor()) >= cst.HORIZONTAL_BORDER-5: # snake hits horizontal border
            
            if self.head.xcor() > 0: # right border
                self.head.goto(x=-cst.HORIZONTAL_BORDER+10, y=self.head.ycor())

            else: # left border
                self.head.goto(x=cst.HORIZONTAL_BORDER-10, y=self.head.ycor())
        
        elif abs(self.head.ycor()) >= cst.VERTICAL_BORDER-5: # snake hits vertical border
            
            if self.head.ycor() > 0: # top border
                self.head.goto(x=self.head.xcor(), y=-cst.VERTICAL_BORDER+10)

            else: # bottom border
                self.head.goto(x=self.head.xcor(), y=cst.VERTICAL_BORDER-10)

    def up(self):
        if self.head.heading() != cst.DOWN:
            self.head.setheading(cst.UP)

    def down(self):
        if self.head.heading() != cst.UP:
            self.head.setheading(cst.DOWN)

    def right(self):
        if self.head.heading() != cst.LEFT:
            self.head.setheading(cst.RIGHT)

    def left(self):
        if self.head.heading() != cst.RIGHT:
            self.head.setheading(cst.LEFT)

    def grow(self):
        new_segment = Turtle("square")
        new_segment.color("chartreuse")
        new_segment.up()
        new_segment.goto(x=self.body[-1].xcor(), y=self.body[-1].ycor())
        self.body.append(new_segment)
