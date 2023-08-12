print('''
888
888
888
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.
888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b
888   888    88888888.d888888"Y8888b.888  888888    88888888
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")

question_1 = input("You're at a cross-road, where do you want to go? Type 'left' or 'right'?\n").lower()
if question_1 == 'right':
    print("Game Over.")
elif question_1 == 'left':
    question_2 = input("You come to a lake, there's an island in the middle of the lake.\n"
                       "Type 'wait' to wait for a boat, type 'swim' to swim across.\n").lower()
    if question_2 == 'swim':
        print("Game over, try again.")
    elif question_2 == 'wait':
        question_3 = input("You arrive at the island unharmed. There's a house with three doors.\n"
                           "Red, Blue and Yellow?.\nWhich color will you choose.\n").lower()
        if question_3 == 'red' or question_3 == 'blue':
            print("Game over, try again.")
        elif question_3 == 'yellow':
            print("You Win!")
