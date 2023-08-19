computer_choice = random.randint(0, 2)
print("Computer choice")
print(game_images[computer_choice])

if user_choice == computer_choice:
    print("It's a Draw ⚖️")
elif user_choice == 0 and computer_choice == 1:
    print("Computer Wins 🎉🏆")
    print("You Lost 😢")
    print("Verdict: 🧻 can wrap 🪨")
elif user_choice == 0 and computer_choice == 2:
    print("You Win 🎉🏆")
    print("Verdict: 🪨 can crush ✂️")
elif user_choice == 1 and computer_choice == 0:
    print("You Win 🎉🏆")
    print("Verdict: 🧻 can wrap 🪨")
elif user_choice == 1 and computer_choice == 2:
    print("Computer Wins 🎉🏆")
    print("You Lost 😢")
    print("Verdict: ✂️ can cut 🧻")
elif user_choice == 2 and computer_choice == 0:
    print("Computer Wins 🎉🏆")
    print("You Lost 😢")
    print("Verdict: 🪨 can crush ✂️")
elif user_choice == 2 and computer_choice == 1:
    print("You Win 🎉🏆")
    print("Verdict: ✂️ can cut 🧻")
