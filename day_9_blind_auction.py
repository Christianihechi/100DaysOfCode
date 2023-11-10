def blind_auction(auction_list):
    highest_bid = 0
    winner = ""

    for name, bid in auction_list.items():
        if bid > highest_bid:
            highest_bid = bid
            winner = name

    print(f"The winner is {winner} with a ${highest_bid} bid.")


print("Welcome to the Secret Auction Program")
user_auctions = {}

# Loop to collect new bids or stop
while True:
    user_name = input("What is your name: ").title()
    bid_amount = int(input("What is your bid: "))

    user_auctions[user_name] = bid_amount

    new_bid = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if new_bid != 'yes':
        break

blind_auction(user_auctions)
