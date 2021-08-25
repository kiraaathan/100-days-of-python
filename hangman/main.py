# hangman game implemented in python

from os import system, name
from wordlist import *
from ascii_art import *
import random


def clear():
    if name == "posix":
        system("clear")
    else:
        system("cls")


end_of_game = False
lives = 6
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = ["_"] * word_length
previous_guess = []

print(logo)

# game logic
while not end_of_game:
    user_guess = input("Guess a letter: ").lower()
    clear()

    if user_guess in previous_guess:
        print("You've already guessed this letter. Try something else!")
    else:
        previous_guess += user_guess

    guess_is_right = False
    for i in range(word_length):
        if user_guess == chosen_word[i]:
            guess_is_right = True
            display[i] = user_guess

    print(" ".join(display))

    if guess_is_right:
        if "_" not in display:
            print(f"Congratulations! You win! The word was {chosen_word}")
            end_of_game = True
    else:
        lives -= 1
        print(f"You guessed {user_guess}. It is not in the word. You lose a life!")
        if lives == 0:
            print(f"you lose! The word was {chosen_word}. Game over!")
            end_of_game = True

    print(stages[lives])
