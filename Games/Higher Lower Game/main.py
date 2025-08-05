from art import logo
import stuffs as stf
import game_data

stop = False
print(logo)

while not stop:
    you_right = True
    score = 0
    data = game_data.data.copy()
    A, B = stf.get_versus(data)

    while you_right and data:
        stf.display_versus(A, B)
        answer = stf.get_answer(A, B)
        if answer:
            score += 1
            print("\n" + "*" * 48 + " You're right ✅ " + "*" * 49)
            print("\n" + " " * 48 + f"Current score : {score}")
            A, B, data = stf.update_versus(A, B, data)
        else:
            print("\n" + "*" * 50 + " You lose 💔 " + "*" * 51)
            print("\n" + " " * 48 + f"Final score : {score}")
            you_right = False

    stop = stf.play_again()
