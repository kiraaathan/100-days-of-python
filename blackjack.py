# Black Jack
import random

# User hands

ufirst_hand = random.randint(1, 10)
usecond_hand = random.randint(1, 10)
uthird_hand = random.randint(1, 2)
print(f"Your hands are : {ufirst_hand} & {usecond_hand}")

# Computer hands

cfirst_hand = random.randint(1, 10)
csecond_hand = random.randint(1, 2)
print(f"Opponents hands are : {cfirst_hand}")


# Ace

if ufirst_hand == 1 or cfirst_hand == 1:
    ufirst_hand = cfirst_hand = 11

if usecond_hand == 1:
    uecond_hand = 11
    sum = ufirst_hand + usecond_hand
    if sum > 21:
        usecond_hand = 1

if csecond_hand == 1:
    csecond_hand = 11
    sum = cfirst_hand + csecond_hand
    if sum > 21:
        csecond_hand = 1

if uthird_hand == 1:
    uthird_hand = 11

# Sum
sum_user_hands = ufirst_hand + usecond_hand
sum_c_hands = cfirst_hand + csecond_hand

choice = input("Do you want to take another card  (Y/N) :")

if choice == "y" or choice == "Y":
    sum_user_hands += uthird_hand
    print(f"Your third card is {uthird_hand}")
    print(f"Opponent final cards are {cfirst_hand} & {csecond_hand}")
    print(f"Your final cards are {ufirst_hand} {usecond_hand} & {uthird_hand}\n")
    print(f"Sum user hand : {sum_user_hands}")
    print(f"Sum opponent hand : {sum_c_hands} ")
    if sum_user_hands > 21:
        print("You lost!")
        exit()
    else:
        if sum_c_hands > sum_user_hands:
            print("You lost")
            exit()
        else:
            print("You win")
            exit()
else:
    print(f"Opponent final cards are {cfirst_hand} & {csecond_hand}")
    print(f"Your final cards are {ufirst_hand} & {usecond_hand}\n")
    print(f"Sum user hand : {sum_user_hands}")
    print(f"Sum opponent hand : {sum_c_hands} ")
if sum_user_hands > sum_c_hands:
    print("You win!")
else:
    print("You lose!")
