import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreborad import ScoreBoard

# Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Objects
paddle1 = Paddle(350)
paddle2 = Paddle(-350)
ball = Ball()
scoreboard = ScoreBoard()

# key bidings
screen.onkeypress(paddle1.go_up, "Up")
screen.onkeypress(paddle1.go_down, "Down")
screen.onkeypress(paddle2.go_up, "z")
screen.onkeypress(paddle2.go_down, "s")
screen.listen()

# Game loop
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect left paddle misses
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.mainloop()
