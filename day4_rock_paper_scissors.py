import random
print("Rock Paper Scissors Game.\nWhich do you choose: 0, 1, or 2?\n")
print("0 - 🪨Rock\n1 - 🧻Paper\n2 - ✂️Scissors\n")
rock = '''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
Rock
'''
paper = '''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'    
Paper
'''
scissors = '''
  _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.
Scissors
'''

game_images = [rock, paper, scissors]
user_choice = int(input("Enter your choice here: "))
if user_choice >= 3 or user_choice < 0:
    print("Opps! You entered an invalid number! Enter 0, 1, or 2.")
else:
    print("Your choice")
    print(game_images[user_choice])

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
