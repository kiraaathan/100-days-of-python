import random
import hangman_word
import hangman_art

# hangman logo
print(hangman_art.logo)

lives = 6
chosen_word = random.choice(hangman_word.word_list)
display = []

# Blank space

for letter in range(len(chosen_word)):
    display += "_"
end_of_game = False

# Game function

while not end_of_game:
    guess = input("Guess the letter : ").lower()
    if guess in display:
        print("Already guessed the letter")
    else:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        if guess not in chosen_word:
            lives -= 1
        if lives == 0:
            end_of_game = False
            print("You lost!")
        if "_" not in display:
            end_of_game = True
            print("\nYou win!")
        print(display)

        # Hangman lives

        print(hangman_art.stages[lives])
