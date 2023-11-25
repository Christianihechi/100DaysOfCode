import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def game_start():
    extra_user_card = 2
    extra_comp_card = 2
    random_comp_cards = random.sample(cards, extra_comp_card)
    random_user_cards = random.sample(cards, extra_user_card)

    def add_user_cards(rand_user):
        sum_user = sum(rand_user)
        return sum_user

    def add_comp_cards(rand_comp):
        sum_comp = sum(rand_comp)
        return sum_comp

    print(f"Your cards: {random_user_cards}, Current score: {add_user_cards(random_user_cards)}")
    print(f"Dealer's first card: {random_comp_cards[0]}")
    extra_card = input("Do you want an extra card? Type 'y' or 'n': ").lower()

    while add_comp_cards(random_comp_cards) < 17:
        random_comp_cards.append(random.choice(cards))

    if extra_card == 'y':
        # Append the extra card to the existing random_user_cards
        random_user_cards.append(random.choice(cards))

        if 11 in random_user_cards and sum(random_user_cards) > 21:
            if 11 in random_user_cards:
                random_user_cards[random_user_cards.index(11)] = 1
        else:
            if 11 in random_user_cards:
                random_user_cards[random_user_cards.index(11)] = 11

        # Continue with the rest of the code
        print(f"Your final hand: {random_user_cards}, Final score: {add_user_cards(random_user_cards)}")

        # Check if the dealer's total score is less than 17, then draw an extra card
        while add_comp_cards(random_comp_cards) < 17:
            random_comp_cards.append(random.choice(cards))

        print(f"Dealer's final cards: {random_comp_cards}, Final score: {add_comp_cards(random_comp_cards)}")

    else:
        print(f"Your final hand: {random_user_cards}, Final score: {add_user_cards(random_user_cards)}")
        print(f"Dealer's final cards: {random_comp_cards}, Final score: {add_comp_cards(random_comp_cards)}")

    def compare_cards(user, comp):
        if user > 21:
            print(f"It's a Bust. You lose!")
        elif comp > 21:
            print("Dealer went over. You win!")
        elif user == comp:
            print("Draw")
        elif user > comp:
            print("You win!")
        else:
            print("Dealer wins")

    compare_cards(add_user_cards(random_user_cards), add_comp_cards(random_comp_cards))


start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if start_game == 'y':
    game_start()

while input("Do you want to play again? 'y' or 'n': ").lower() == 'y':
    game_start()
