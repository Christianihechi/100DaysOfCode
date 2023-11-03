import random
from hangman_words import word_list as wl
from hangman_art import stages, logo

# Set word_list to the imported word list
word_list = wl

# Randomly choose a word from word_list
random_words = random.choice(word_list)
chosen_word = random_words

# Display the game logo
print(logo)

# Initialize the display with underscores for each letter in chosen_word
display = ["_" for each_letter in chosen_word]
print(" ".join(display))

# Initialize game variables
end_of_game = False
game_lives = 6

# Start the game loop
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter is already in the display
    if guess in display:
        print(f"You've already guessed {guess}, try another letter.")

    # Check if the guessed letter is not in the chosen word
    if guess not in chosen_word:
        print(f"You guessed '{guess}' and that's not in the word. You lost a dear life.")
        game_lives -= 1
        # Display the current stage of the hangman
        print(stages[game_lives])

    # Update the display with correctly guessed letters
    for position, word_letter in enumerate(chosen_word):
        if word_letter == guess and display[position] == "_":
            display[position] = word_letter
    print(" ".join(display)

    # Check if all letters have been guessed
    if "_" not in display:
        end_of_game = True
        print("You won! The correct word is:")
        result = ("".join(display))
        print(result.upper())
    # Check if the player has run out of lives
    elif game_lives == 0:
        end_of_game = True
        print("Too many wrong entries, you lose!")
