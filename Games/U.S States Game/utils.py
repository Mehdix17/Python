import pandas as pd

# data
data = pd.read_csv("50_states.csv")
all_states = data["state"]
guessed_states = []

def answer_is_correct(answer):
    if answer in all_states.to_list() and answer not in guessed_states:
        return True
    return False

def get_state_cord(state):
    state_row = data[data.state == state]
    x = state_row.x.iloc[0]
    y = state_row.y.iloc[0]
    return x, y

def update_guessed_states(state):
    guessed_states.append(state)
