# Caesar cipher
def encryption(text, shift):
    cipher_text = ""
    for letter in text:
        position = alphabets.index(letter)
        shift_position = position + shift
        cipher_text += alphabets[shift_position]
    print(cipher_text)


def decryption(text, shift):
    cipher_text = ""
    for letter in text:
        position = alphabets.index(letter)
        shift_position = position - shift
        cipher_text += alphabets[shift_position]
    print(cipher_text)


alphabets = [
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
]
choice = input("Press E for encryption and D for decryption:")
if choice != "E" or choice != "e" or choice != "D" or choice != "D":
    print("Invalid choice!")
    exit()
text = input("Enter the text:").lower()
shift = int(input("Enter the shift value:"))
shift = shift % 26

if choice == "E" or choice == "e":
    encryption(text, shift)
elif choice == "D" or choice == "d":
    decryption(text, shift)
else:
    print("Invalid choice!")
