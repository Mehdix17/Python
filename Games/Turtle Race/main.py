from turtle import Turtle, Screen
from random import randint

screen = Screen()
user_width = 800
user_height = 400
screen.setup(width=user_width, height=user_height)
race_on = False

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
turtle_list = []
x_pos = -380
y_pos = 160 

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    turtle_list.append(new_turtle)

for turtle in turtle_list:
    y_pos -= 40 
    turtle.up()
    turtle.goto(x=x_pos, y=y_pos)

while not race_on:
    try:
        user_bet = screen.textinput("Make your bet !", "Which trutle will win the race ? Enter a color : ").lower()
        if user_bet in colors:
            race_on = True
        else:
            print("\nInvalid color ❌")
    except:
        print("\n💡 You have to choose a color")

while race_on:
    
    for turtle in turtle_list:
        turtle.forward(randint(1, 10))
        
        if turtle.xcor() >= user_width/2 -20:
            winning_color = turtle.pencolor()
            
            if user_bet == winning_color:
                print(f"\nYou've won ! The {winning_color} turtle is the winner !")
            
            else:
                print(f"\nYou've lost ! The {winning_color} turtle is the winner !")
            
            race_on = False
            break

screen.mainloop()
