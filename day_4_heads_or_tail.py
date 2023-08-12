import random
print("Virtual Coin Flipper - Heads or Tail")
print("To toss a coin, just run the program\n")

random_coin = random.randint(0,1)

if random_coin == 0:
    print("Heads")
else:
    print("Tails")


