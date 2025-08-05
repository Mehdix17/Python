import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# bidings
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.listen()

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect succesfull crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.update()

screen.mainloop()
