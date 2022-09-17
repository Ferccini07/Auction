import os
from art import logo
print(logo)


bidding_finished = False
bidders = {}


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("Please enter your name: ")
    bid = int(input("Please enter bid: $"))
    bidders[name] = bid
    print(bidders)
    ask = input("Are there other users who want to bid? Write 'yes' or 'no': "
                ).lower()
    if ask == "yes":
        os.system('cls')
    else:
        bidding_finished = True
        find_highest_bidder(bidders)
