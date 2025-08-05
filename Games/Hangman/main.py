from hangman_art import logo, stages
from hangman_words import word_list
import random

print(logo)
game_over = False
guessed_letters = []
lives = 6

word = random.choice(word_list)
user_word = ["_" for _ in range(len(word))]

while not game_over:
    print()
    print("".join(user_word))
    guess = input("\nGuess a letter : ").lower()
    
    if guess in word:

        if guess not in guessed_letters:
            guessed_letters.append(guess)
            for i, _ in enumerate(word):
                if guess == word[i]:
                    user_word[i] = guess
        else:
            print(f"\n💡 You've already guessed {guess}")

    else:
        print(f"\n❌ You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(stages[lives])
        print(f"\nRemaining lives : {lives}")
        

    if word == "".join(user_word):
        game_over = True
        print("\nYou win 👑")

    elif lives == 0:
        game_over = True
        print("\nYou lose 💔")
        print(f"\nThe word was : {word}")
