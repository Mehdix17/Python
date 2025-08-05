import stuffs as stf
import art

stop = False
print(art.logo)
print(stf.welcome_msg)

while not stop:
    guess = 0
    number = stf.generate_random_number()
    difficulty = stf.get_difficulty()
    attempts = stf.set_attemps(difficulty)

    while guess != number and attempts != 0:
        guess = stf.make_guess()
        attempts = stf.eval_guess(number, guess, attempts)

    stop = stf.play_again()
    if not stop:
        print(art.new_game)

print("\nThank you for playing the game! Hope you enjoyed the game. See you next time!")
