# Dice Roller
import random

choice = "Y"
while choice != "N" or choice != "n":
    if choice == "Y" or choice == "y":
        roller = random.randint(1, 6)
        print(f"The outcome is {roller}")
    elif choice == "N" or choice == "n":
        exit(0)
    else:
        print("Invalid entry!")
    choice = input("Do you want to roll again? (Y/N) :")
