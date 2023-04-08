from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
blind_auction = {}
repeat = True


def find_the_highest_bid(blind_auction):
    highest_bid = 0
    for bidder in blind_auction:
        bid = blind_auction[bidder]
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")


while repeat:
    name = input("What's your name? ")
    bid = int(input("What's your bid? "))
    blind_auction[name] = bid

    other_bidders = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bidders == 'yes':
        clear()
    else:
        repeat = False
        find_the_highest_bid(blind_auction)
#print(blind_auction)
# max_bid = max(blind_auction.values())
# winner = max(zip(blind_auction.values(), blind_auction.keys()))[1]
