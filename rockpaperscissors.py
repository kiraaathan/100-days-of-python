# Game rock paper scissors
import random

print("Rules for the game!\n")
print(
    "* Rock wins over scissors\n* Paper wins over Rocks\n* Scissors wins over Paper\n"
)
print("How to play the game!\n")
print("Press \n 0 for Rock \n 1 for paper \n 2 for scissors")
print("\nEnter your hand : ")
user_hand = int(input())
random_hand = int(random.randint(0, 2))
print("Opponent played :")
print(random_hand)
if user_hand > 2:
    print("Invalid entry!")
else:
    if random_hand == user_hand:
        print("Draw Match!")
    elif random_hand > user_hand:
        if user_hand == 2 and random_hand == 1:
            print("You win!")
        else:
            print("You lose!")
    elif random_hand < user_hand:
        if user_hand == 0 and random_hand == 2:
            print("You lose!")
        else:
            print("You win!")
