print("Welcome to the Secret Auction Program")
user_auctions = {}

# Loop to collect new bids or stop
while True:
    user_name = input("What is your name: ").title()
    bid_amount = int(input("What is your bid: "))

    new_bid = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    user_auctions[user_name] = bid_amount

    if new_bid != 'yes':
        break

# Find highest bid

highest_bid = 0
winner = ""

if user_auctions[user_name] > highest_bid:
    highest_bid = user_auctions[user_name]
    winner = user_name

print(f"The winner is {winner} with a ${highest_bid} bid.")
