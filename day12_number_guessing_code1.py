from random import randint

random_number = randint(1, 101)
game_end = False

easy_attempts = 10
hard_attempts = 5


def start_game():
    print(f"Welcome To The Number Guessing Game\n"
          f"I'm thinking of a number between 1 and 100. {random_number}")

    game_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if game_level == 'easy':
        easy()
    elif game_level == 'hard':
        hard()


def easy():
    global easy_attempts
    print(f"You have {easy_attempts} attempts remaining to guess the number.")
    while easy_attempts != 0:
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print(f"You won, {guess} is the right number!")
            break  # End the loop if the guess is correct

        if guess < random_number:
            easy_attempts -= 1
            print('Too low')

        elif guess > random_number:
            easy_attempts -= 1
            print('Too high')

        if easy_attempts != 0:
            print("Guess again.")  # Displayed only if the guess is incorrect
            print(f"You have {easy_attempts} attempts remaining to guess the number.")

    if easy_attempts == 0:
        print("You lost, you're out of guesses.")


def hard():
    global hard_attempts
    print(f"You have {hard_attempts} attempts remaining to guess the number.")
    while hard_attempts != 0:
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print(f"You won, {guess} is the right number!")
            break  # End the loop if the guess is correct

        if guess < random_number:
            hard_attempts -= 1
            print('Too low')
        elif guess > random_number:
            hard_attempts -= 1
            print('Too high')

        if hard_attempts != 0:
            print("Guess again.")  # Displayed only if the guess is incorrect
            print(f"You have {hard_attempts} attempts remaining to guess the number.")

    if hard_attempts == 0:
        print("You lost, you're out of guesses.")


# Call the start_game function to begin the game
start_game()
