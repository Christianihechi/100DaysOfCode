print('''
       ^^      ..                                       ..
              []                                       []
            .:[]:_          ^^                       ,:[]:.
          .: :[]: :-.                             ,-: :[]: :.
        .: : :[]: : :`._                       ,.': : :[]: : :.
      .: : : :[]: : : : :-._               _,-: : : : :[]: : : :.
  _..: : : : :[]: : : : : : :-._________.-: : : : : : :[]: : : : :-._
  _:_:_:_:_:_:[]:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:[]:_:_:_:_:_:_
  !!!!!!!!!!!![]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!![]!!!!!!!!!!!!!
  ^^^^^^^^^^^^[]^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^[]^^^^^^^^^^^^^
              []                                       []
              []                                       []
              []                                       []
      ''')
print("Welcome to the Jumping game")
print("Jump until you win!")
choice1 = input("You're about to cross a bridge and aren't sure if you can jump across. "
                "Type 'Jump' or 'Skip': ").lower()
if choice1 == 'jump':
    print("You've got some faith. You made it!")
    choice2 = input("There's a ship coming to your direction.\n"
                    "Type 'Join' to join them or 'Swim' to swim away: ").lower()
    if choice2 == 'swim':
        print("You made it on your own.")
        choice3 = input("You find three colored boxes and can only pick one. "
                        "Type 'Red', 'Blue', or 'Yellow' to choose.\n").lower()
        if choice3 == 'red':
            print("Oh no! You can't go home until after 100 years in the island.")
        elif choice3 == 'blue':
            print("You'll be rescued after 10 years. be hopeful!")
        else:
            print("Congratulations! You made it! A big ship is on its way to save you! ")
    else:
        print("Sorry. You were kidnapped by some insurgents!")

else:
    print("You failed. You were hit by a car on the bridge!")
