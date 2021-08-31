from os import name, system
from art import blackjack_logo
import random
import time


def clear():
    if name == "posix":
        system("clear")
    else:
        system("cls")


def deal_cards(cards):
    time.sleep(0.5)
    return random.choices(cards, k=2)


def draw_next_card(cards):
    time.sleep(0.5)
    return random.choice(cards)


def get_confirmation_to_play():
    while True:
        user_input = input("Do you want to play a game of Blackjack? (y/n)\n").lower()
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        else:
            print("Invalid choice. Try again, please.")


def continue_to_draw():
    while True:
        user_input = input("You wanna draw another card? (y/n)\n").lower()
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        else:
            print("Invalid choice. Try again, please.")


def get_score(hand):
    score = 0
    has_ace = False
    for card in hand:
        if card == 11:
            has_ace = True
        score += card
    if score > 21 and has_ace == True:
        score = score - 10
    return score


def check_score(player, computer):
    print("checking score...")
    if computer["score"] > 21:
        print("You win. Computer went over 21!")
    elif computer["score"] > player["score"]:
        print(f"Computer beats you!")
        print(f"Computer\n hand: {computer['cards']} score: {computer['score']}")
        print(f"You\n hand: {player['cards']} score: {player['score']}")
    else:
        print(f"You beat the computer!")
        print(f"Computer\n hand: {computer['cards']} score: {computer['score']}")
        print(f"You\n hand: {player['cards']} score: {player['score']}")


def show_player_info(player):
    print(f"your hand: {player['cards']}, your score is {player['score']}.")


def play_game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    player = {"cards": [], "score": 0}
    computer = {"cards": [], "score": 0}
    print(blackjack_logo)
    print("Dealing cards...")
    player["cards"] = deal_cards(cards)
    computer["cards"] = deal_cards(cards)
    player["score"] = get_score(player["cards"])
    computer["score"] = get_score(computer["cards"])
    print(f"computer's first card: {computer['cards'][0]}")
    show_player_info(player)
    while continue_to_draw():
        player["cards"].append(draw_next_card(cards))
        player["score"] = get_score(player["cards"])
        show_player_info(player)
        if player["score"] > 21:
            print("You went over. You lose. Game over!")
            break
    else:
        check_score(player, computer)
