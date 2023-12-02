from random import randint
answer = randint(1, 100)

# Setting the values for each level as a constant
EASY_LEVEL = 10
HARD_LEVEL = 5


# Asking the user to choose a difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL


# Check the user's guess against the actual random number.
def check_answer(guess, answer):
    if guess > answer:
        print('Too high')
    elif guess < answer:
        print('Too low')
    else:
        print(f"You got it. The correct number is {answer}.")


def game():
    # Choosing a random number from 1-100

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"The correct answer is {answer}. Just for help!")

    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to make a guess. ")

    # Asking the user to guess a number
    while turns != 0:
        # Track the number of turns and reduce by 1 if the guess is wrong
        guess = int(input("Make your guess: "))
        if guess == answer:
            return print(f"You won, {guess} is the right number!")


        if guess < answer or guess > answer:
            turns -= 1
            check_answer(guess, answer)
            if turns == 0:
                print("You have run out of attempts. You lose!")
                return
            else:
                print("Guess again.")
        print(f"You have {turns} attempts remaining. ")


game()
