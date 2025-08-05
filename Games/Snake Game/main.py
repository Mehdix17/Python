import constants as cst
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBorad
from draw_screen import ScreenDrawer

# screen
screen = Screen()
screen.setup(width=cst.SCREEN_WIDTH, height=cst.SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Objects
screen_drawer = ScreenDrawer()
snake = Snake()
food = Food()
scoreboard = ScoreBorad()

# key bidings
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# azerty keybord
screen.onkey(snake.up, "z")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "q")

screen.listen()

# Game loop
game_is_on = True

while game_is_on:
    screen.update()
    snake.move()
    
    # check if there is a collision between the snake and food
    if snake.head.distance(food) <= 20:
        food.spawn()
        snake.grow()
        scoreboard.increase_score()
    
    # check if there is a collision between the snake and its tail
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 1:
            scoreboard.reset()
            snake.reset()

screen.mainloop()
