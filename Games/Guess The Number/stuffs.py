from random import randint

welcome_msg = "\nWelcome to the Number Guessing Game!"

difficulty_msg = """
I'm thinking of a number between 1 and 100.

Choose a difficulty : 'easy', 'medium' or 'hard'"""

def generate_random_number():
    return randint(1, 100)

def get_difficulty():
    print(difficulty_msg)
    while True:
        difficulty = input("\nDifficulty : ").lower()
        if difficulty not in ('easy', 'medium', 'hard'):
            print("\n💡 Please type : 'easy', 'medium' or 'hard'")
        else:
            return difficulty

def set_attemps(difficulty):
    match difficulty:
        case "easy": return 10
        case "medium": return 7
        case "hard": return 5

def make_guess():
    while True:
        try:
            guess = int(input("\nMake a guess : "))
            if guess not in range(1,101):
                print("\n💡 Please make a guess between 1 and 100")
            else:
                break
        except:
            print("\n💡 Please make a guess between 1 and 100")
    return guess

def eval_guess(number, guess, attempts):
    if guess != number:
        if guess > number:
            print("\nToo high")
        elif guess < number:
            print("\nToo low")
        attempts -= 1
        if attempts == 0:
            print("\nYou've run out of guesses, you lose 💔")
            print(f"\nThe number was {number}")
        else:
            print(f"\nYou have {attempts} attempts remaining to guess the number")
    else:
        print(f"\nYou got it! The answer was {number} 👑")
    return attempts

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
