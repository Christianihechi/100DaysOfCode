import random

print("Banker Roulette")

names_string = input("Type the names of each person, followed by a space.\nPress 'Enter' when done.\n:").title()
names = names_string.split(" ")

# Get length of the list
ran_length = len(names)
# Set last integer of random to the length of list
ran_picked = random.randint(0, ran_length)
#  Add random number as index to list
name_picked = names[ran_picked]

print(f"Wow! {name_picked}, you're going to pay for the meal today!")
