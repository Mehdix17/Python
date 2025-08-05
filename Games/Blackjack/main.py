import stuffs as stf
from art import logo

stop = False

while not stop:
    
    print(logo)
    user_hand = []
    computer_hand = []
    user_score = 0
    computer_score = 0
    user_hand.extend(stf.draw_random_card(2))
    computer_hand.extend(stf.draw_random_card(2))

    while True:
        
        user_score = stf.calcul_hand_score(user_hand)
        computer_score = stf.calcul_hand_score(computer_hand)
        stf.display_hands(user_hand, user_score, computer_hand, computer_score, "normal")

        if stf.check_blackjack(user_hand, computer_hand):
            break
        else:
            if stf.check_bust(user_hand, user_score):
                break
            else: # user_score <= 21
                if stf.get_another_card():
                    user_hand.extend(stf.draw_random_card(1))
                else:
                    computer_hand, computer_score = stf.computer_plays(computer_hand, computer_score)
                    if stf.check_bust(computer_hand, computer_score):
                        print("\nComputer went over. You win 👑")
                        break
                    stf.display_hands(user_hand, user_score, computer_hand, computer_score, "final")
                    stf.display_winner(user_score, computer_score)
                    break

    stop = stf.play_again()

print("\nThank you for playing Blackjack! Hope you enjoyed the game. See you next time!")
