import turtle
import utils
from scoreborad import ScoreBoard
from state_writer import Writer

# Setup
screen = turtle.Screen()
screen.title("U.S states")
screen.setup(width=750, height=600)
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

# Objects
scoreborad = ScoreBoard()
writer = Writer()

# Game loop
on_game = True

while on_game:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name ?").title()
    
    if utils.answer_is_correct(answer_state):
        x, y = utils.get_state_cord(answer_state)
        writer.write_state(answer_state, x, y)
        utils.update_guessed_states(answer_state)
        scoreborad.update_score()
    
    else:
        writer.game_over()
        on_game = False

screen.mainloop()
