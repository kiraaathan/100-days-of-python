# silent auction

import os


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def find_highest_bidder(bidders):
    highest_bid = 0
    hightest_bidder = ""
    for i in bidders:
        if bidders[i] > highest_bid:
            highest_bid = bidders[i]
            hightest_bidder = i
    return (highest_bid, hightest_bidder)


bidders = {}
bidding_status = True

while bidding_status == True:
    try:
        name = input("What is your name?\n")
        bid = int(input("what's the bidding amount?\n"))

        bidders[name] = bid
        result = input(
            "Are there more bidders? (type 'yes' if there are more)\n"
        ).lower()
        if result != "yes":
            bidding_status = False
        clear()

    except ValueError:
        print("Enter a valid bid!")

(highest_bid, highest_bidder) = find_highest_bidder(bidders)
print(f"WINNER \nbidder: {highest_bidder}\nbid amount: {highest_bid}!")
