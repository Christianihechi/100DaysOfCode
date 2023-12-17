from higher_lower_game_art import vs, logo
from higher_lower_gamedata import data
from os import system, name
import random


# define our clear function
def clear():
    # for windows the os.name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # Mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')


# Track the user score and gameplay to repeat
score = 0
game_end = False


# Format the account data into printable format
def format_data(account):
    """Format the Instagram accounts data into printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc} from {account_country}."


def game():
    """Main game function"""
    global game_end
    account_b = random.choice(data)
    print(logo)

    while not game_end:
        # Get a random accounts from the game data
        account_a = account_b

        if account_a == account_b:
            account_b = random.choice(data)

        # Print formatted data and VS logo
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        # Ask the user for a guess
        print()
        guess = input("Who has more Instagram followers? Type 'A' or 'B': ").lower()
        clear()
        print(logo)
        # Check if user guess is correct
        def check_guess(user_guess):

            # Access and modify global variables
            global score, game_end
            """Checks the user's guess against the Instagram account follower counts"""
            if user_guess == 'a':
                if account_a["follower_count"] > account_b["follower_count"]:
                    score += 1
                    return f"You're correct! Current Score: {score}"
                else:
                    game_end = True
                    return f"Sorry, you failed! Final Score: {score}"
            elif user_guess == 'b':
                if account_b["follower_count"] > account_a["follower_count"]:
                    score += 1
                    return f"You're correct! Current Score: {score}"
                else:
                    game_end = True
                    return f"Sorry, you failed! Final Score: {score}"
            else:
                return f"You entered an invalid input"

        result = check_guess(guess)
        print(result)


game()
