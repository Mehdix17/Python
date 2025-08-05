import random

normal_hand_msg = """
Your hand : {}
Current score : {}
Computer's first card : {}"""

final_hand_msg = """
Your final hand : {}
Your Final score: {}

Computer's final hand : {}
Computer's Final score: {}"""

def draw_random_card(amount):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choices(cards, k=amount)

def calcul_hand_score(hand):
    return sum(hand)

def display_hands(user_hand, user_score, computer_hand, computer_score, mode):
    if mode == "normal":
        print(normal_hand_msg.format(user_hand, user_score, computer_hand[0]))
    else: # final
        print(final_hand_msg.format(user_hand, user_score, computer_hand, computer_score))
          
def check_blackjack(user_hand, computer_hand):
    
    def checker(hand, msg):
        if len(hand) == 2 and calcul_hand_score(hand) == 21:
            print(msg)
            return True
        else:
            return False
    
    blackjack_msg = ["\nYou have a blackjack, you win 🔥", "\nComputer has a blackjack, you lose 🤖"]
    return checker(user_hand, blackjack_msg[0]) or checker(computer_hand, blackjack_msg[1])

def check_bust(hand, score):
    if score > 21:
        if 11 in hand:
            index = hand.index(11)
            hand[index] = 1
            score = calcul_hand_score(hand)
            if score > 21:
                print("\nYou went over. You lose 😭")
                return True
            return False
        else:
            print("\nYou went over. You lose 😭")
            return True
    return False

def get_another_card():
    print("\nDo you want to draw another card ? (Y|N)")
    while True:
        answer = input("\nYour answer : ").lower()
        if answer not in ("yes", "no", "y", "n"):
            print("\n💡 Please answer by 'yes' or 'no'")
        else:
            if answer in ("yes", "y"):
                return True
            else:
                return False

def computer_plays(computer_hand, computer_score):
    while computer_score < 17:
        computer_hand.extend(draw_random_card(1))
        computer_score = calcul_hand_score(computer_hand)
    return computer_hand, computer_score

def display_winner(user_score, computer_score):
    if user_score > computer_score:
        print("\nYou win 👑")
    elif user_score < computer_score:
        print("\nYou lose 💔")
    else:
        print("\nDraw 🤝")

def play_again():
    print("\nDo you want to play a new game ? (Y|N)")
    while True:
        answer = input("\nYour answer : ").lower()
        if answer not in ("yes", "no", "y", "n"):
            print("\n💡 Please answer by 'yes' or 'no'")
        else:
            if answer in ("yes", "y"):
                return False
            else:
                return True
