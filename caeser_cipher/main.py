# Ceaser Cipher

from art import logo


def encode_decode(message, shift_key, user_choice):
    modded_message = ""

    if user_choice == "decode":
        shift_key = -shift_key

    for i in message:
        if i.isupper():
            # ascii code for A-Z begins from 65
            modded_message += chr((ord(i) + shift_key - 65) % 26 + 65)
        elif i.islower():
            # ascii code for a-z begins from 97
            modded_message += chr((ord(i) + shift_key - 97) % 26 + 97)
        else:
            # special characters and numbers are unaffected
            modded_message += i

    return modded_message


cipher_status = True
print(logo)

while cipher_status == True:
    try:
        user_choice = input(
            "Type 'encode' to encrypt and 'decode' to decrypt: "
        ).lower()
        if user_choice != "encode" and user_choice != "decode":
            raise ValueError
        message = input("Enter the message you want to encode/decode: ")
        shift = input("Enter the shift key: ")

        shift = int(shift) % 26
        modded_message = encode_decode(message, shift, user_choice)
        print(f"Modded message is: \n{modded_message}")
        user_discontinue = input("Do you want to stop? (type yes to stop): ")
        if user_discontinue == "yes":
            print("Goodbye Human! Stay safe.")
            cipher_status = False

    except ValueError:
        print("Invalid entry. Please try again!")
