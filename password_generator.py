# a simple password generator
import string
import random


def get_length():
    while True:
        length = input("Enter the length of the password you want to generate: ")
        try:
            length = int(length)
            if length < 0:
                raise ValueError
            return length
        except ValueError:
            print("Invalid length. Please try again.")


def generate_password(length):
    password = ""
    random_source = string.ascii_letters + string.digits + string.punctuation
    for i in range(length):
        password += random.choice(random_source)
    password = list(password)
    random.shuffle(password)
    password = "".join(password)
    return password


length = get_length()
password = generate_password(length)
print(f"Generated password is {password}")
