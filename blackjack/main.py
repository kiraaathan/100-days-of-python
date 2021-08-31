# implementation of blackjack game in python

from library import *


def main():
    if get_confirmation_to_play():
        play_game()
    else:
        print("Have a good day, human!")


main()
