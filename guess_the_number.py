# Guess the number
LOWER_LIMIT = 1
UPPER_LIMIT = 10
PROXIMITY = 2
SECRET_NUMBER = 6

mode = input("Choose the level to be easy or hard (E/H) : ")
match mode:
    case "E" | "e":
        rounds = 3
    case "H" | "h":
        rounds = 2
    case _:
        print("Are you dumb!")

while rounds != 0:
    print(f"You have only {rounds} chances!")
    number = int(input("Guess the number between 1-10:"))
    if number > UPPER_LIMIT or number < LOWER_LIMIT:
        print("Invalid entry!")
    else:
        if number == SECRET_NUMBER:
            print(f"Good job! You are right! The secret number is {number}")
            exit(0)
        if number > SECRET_NUMBER + PROXIMITY:
            print("Too high!")
        elif number < SECRET_NUMBER - PROXIMITY:
            print("Too low!")
        elif number >= SECRET_NUMBER - PROXIMITY or number <= SECRET_NUMBER + PROXIMITY:
            print("Too closer!")
    rounds = rounds - 1
print("GAME OVER!")
