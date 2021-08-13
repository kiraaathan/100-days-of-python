# Game rockpaperscissors
import random

print("Rules for the game!")
print("Press \n 0 for Rock \n 1 for paper \n 2 for scissor")
print("Enter your hand : ")
user_hand = int(input())
random_hand = int(random.randint(0, 2))
print("Opponent played :")
print(random_hand)
if random_hand == user_hand:
    print("Draw!")
elif random_hand > user_hand:
    print("You lose!")
elif random_hand < user_hand:
    print("You win!")
else:
    print("Invalid entry!")
