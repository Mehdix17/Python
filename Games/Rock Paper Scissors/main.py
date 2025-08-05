import stuffs as stf

print(stf.welcome_msg)
rematch_var = True

while rematch_var:
    user_score = 0
    computer_score = 0
    winning_rounds_number = stf.winning_rounds_number_selector()

    while user_score != winning_rounds_number and computer_score != winning_rounds_number:

        user_play = stf.user_play_choice()
        computer_play = stf.computer_play_generator()
        round_winner = stf.calculate_round_winner(user_play, computer_play)
        user_score, computer_score = stf.update_score(user_score, computer_score, round_winner)

    stf.display_winner(user_score, winning_rounds_number)
    rematch_var = stf.rematch()

print(stf.bye_msg)
