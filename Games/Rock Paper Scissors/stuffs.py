import random

# ----------------------------------------------------- Messages -----------------------------------------------------

welcome_msg = r"""

██████████████████████████
█▄─▄▄▀█─▄▄─█─▄▄▄─█▄─█─▄███
██─▄─▄█─██─█─███▀██─▄▀████
▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀
█████████████████████████████████
█▄─▄▄─██▀▄─██▄─▄▄─█▄─▄▄─█▄─▄▄▀███
██─▄▄▄██─▀─███─▄▄▄██─▄█▀██─▄─▄███
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀
██████████████████████████████████████████████
█─▄▄▄▄█─▄▄▄─█▄─▄█─▄▄▄▄█─▄▄▄▄█─▄▄─█▄─▄▄▀█─▄▄▄▄█
█▄▄▄▄─█─███▀██─██▄▄▄▄─█▄▄▄▄─█─██─██─▄─▄█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀

Welcome to the Rock Paper Scissors Game !"""

user_play_msg = """
Press 1 or R to play Rock 🪨

Press 2 or P to play Paper 🗒️

Press 3 or S to play scissors ✂️"""

rock = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = r"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = r"""
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

lose_msg = """

▓██   ██▓ ▒█████   █    ██     ██▓     ▒█████    ██████ ▓█████     ▐██▌ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓██▒    ▒██▒  ██▒▒██    ▒ ▓█   ▀     ▐██▌ 
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒██░    ▒██░  ██▒░ ▓██▄   ▒███       ▐██▌ 
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ▒██░    ▒██   ██░  ▒   ██▒▒▓█  ▄     ▓██▒ 
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░██████▒░ ████▓▒░▒██████▒▒░▒████▒    ▒▄▄  
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░    ░▀▀▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░    ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░    ░  ░ 
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░ ░   ░ ░ ░ ▒  ░  ░  ░     ░          ░ 
 ░ ░         ░ ░     ░            ░  ░    ░ ░        ░     ░  ░    ░                                                                                                                         
"""

win_msg = """

██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗    ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║    ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║    ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║    ╚═╝
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║    ██╗
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝    ╚═╝                                                           
"""

bye_msg = """

██████╗ ██╗   ██╗███████╗    ██████╗ ██╗   ██╗███████╗       ██╗ 
██╔══██╗╚██╗ ██╔╝██╔════╝    ██╔══██╗╚██╗ ██╔╝██╔════╝    ██╗╚██╗
██████╔╝ ╚████╔╝ █████╗      ██████╔╝ ╚████╔╝ █████╗      ╚═╝ ██║
██╔══██╗  ╚██╔╝  ██╔══╝      ██╔══██╗  ╚██╔╝  ██╔══╝      ██╗ ██║
██████╔╝   ██║   ███████╗    ██████╔╝   ██║   ███████╗    ╚═╝██╔╝
╚═════╝    ╚═╝   ╚══════╝    ╚═════╝    ╚═╝   ╚══════╝       ╚═╝                  
"""

# ----------------------------------------------------- Functions -----------------------------------------------------

def winning_rounds_number_selector():
    while True:
        try:
            winning_rounds_number = int(input("\nSelect how many winning rounds you want to play in : "))
            if winning_rounds_number <= 0:
                print("\n❌ Please enter a positive number")
            else:
                print(f"\nOk let's play in {winning_rounds_number} winning rounds ⚔️")
                return winning_rounds_number
        except:
            print("\n❌ Please enter an integer")


def user_play_choice():
    print(user_play_msg)
    while True:
        user_play = input("\nYou : ")
        if user_play.upper() not in ("1", "2", "3", "R", "P", "S"):
            print("\n❌ Please enter a valid play")
        else:
            if user_play == "1" or user_play.upper() == "R":
                print(rock)
                return "R"
            elif user_play == "2" or user_play.upper() == "P":
                print(paper)
                return "P"
            elif user_play == "3" or user_play.upper() == "S":
                print(scissors)
                return "S"

def computer_play_generator():
    computer_play = random.choice(["R", "P", "S"])
    print("\nComputer :\n")
    if computer_play == "R":
        print(rock)
    elif computer_play == "P":
        print(paper)
    else:
        print(scissors)
    return computer_play

def calculate_round_winner(user_play, computer_play):

    if user_play == computer_play:
        return 0
    
    else:
        
        if user_play == "R":
            return 1 if computer_play == "S" else -1

        if user_play == "P":
            return 1 if computer_play == "R" else -1

        if user_play == "S":
            return 1 if computer_play == "P" else -1

def update_score(user_score, computer_score, round_winner):
    if round_winner != 0:
        if round_winner == 1:
            user_score += 1
        elif round_winner == -1:
            computer_score += 1
    print(f"\nScore : {user_score} - {computer_score}")
    return user_score, computer_score
    
def display_winner(user_score, winning_rounds_number):
    print(win_msg) if user_score == winning_rounds_number else print(lose_msg)
    
def rematch():
    print("Do you wanna play again ? (Y|N)")
    while True:
        answer = input("\nYour answer : ").lower()
        if answer in ("y", "yes", "yup", "oui", "n", "no", "nope", "non"):
            if answer in ("y", "yes", "yup", "oui"):
                return True
            else:
                return False
        else:
            print("\n❌ Incorrect answer")
