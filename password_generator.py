# Passwod generator
import random

print("Password geneterator")
print("How many  letters you need:")
l_choice = int(input())
print("How many numbers you need:")
n_choice = int(input())
print("How many symbols you need:")
s_choice = int(input())

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

digits = ["0", "1", "2", "3", "4", "4", "5", "6", "7", "8", "9"]

symbols = ["!", " @", "#", "%", "^", "&", "*", "(", ")", "-", "+"]

password = []
for p in range(1, l_choice + 1):
    password.append(random.choice(letters))
for p in range(1, n_choice + 1):
    password.append(random.choice(digits))
for p in range(1, s_choice + 1):
    password.append(random.choice(symbols))

random.shuffle(password)
pshuffled = ""
for i in password:
    pshuffled += i
print("Generated password is : " + pshuffled)
