import random
from hangman_words import word_list as wl
from hangman_art import stages, logo
word_list = wl
random_words = random.choice(word_list)
chosen_word = random_words
print(logo)
# print(f"Random word is {chosen_word}")

# Initialize display with underscores for each letter in chosen_word
display = ["_" for each_letter in chosen_word]
print(" ".join(display))

print()

end_of_game = False
game_lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}, try another letter.")
    if guess not in chosen_word:
        print(f"You guessed '{guess}' and that's not in the word. You lost a dear life.")
        game_lives -= 1
        print(stages[game_lives])
    for position, word_letter in enumerate(chosen_word):
        if word_letter == guess and display[position] == "_":
            display[position] = word_letter
    print(" ".join(display))

    if "_" not in display:
        end_of_game = True
        print("You won! The correct word is:")
        result = ("".join(display))
        print(result.upper())
    elif game_lives == 0:
        end_of_game = True
        print("Too many wrong entries, you loose!")
