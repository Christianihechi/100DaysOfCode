print("Welcome to the Love Calculator!")
name_1 = input("What is your name: ")
name_2 = input("What is their name: ")

# Convert the input to lower cases
lower_case = name_1.lower() + name_2.lower()

# Add both names together
both_names = lower_case

# Check for the occurrence of 'true and love' separately in the two names
# Check for 'True'
check_t1 = both_names.count('t')
check_r2 = both_names.count('r')
check_u3 = both_names.count('u')
check_e4 = both_names.count('e')

# Check for 'Love'
check_l5 = both_names.count('l')
check_o6 = both_names.count('o')
check_v7 = both_names.count('v')
check_e8 = both_names.count('e')

# Add the counts from each checks
true_check = (check_t1 + check_r2 + check_u3 + check_e4)
love_check = (check_l5 + check_o6 + check_v7 + check_e8)
# Convert the counts to two digits
sum_counts = f"{true_check}{love_check}"
sum_counts = int(sum_counts)


if sum_counts < 10 or sum_counts > 90:
    print(f'Hi,\n{name_1.title()}\n{name_2.title()}\nYour score is {sum_counts}, you go together like coke and mentos.')
elif sum_counts >= 40 and sum_counts <= 50:
    print(f'Hi,\n{name_1.title()}\n{name_2.title()}\nYour score is {sum_counts}, you are alright together.')
else:
    print(f'Hi,\n{name_1.title()}\n{name_2.title()}\nYour score is {sum_counts}.')
