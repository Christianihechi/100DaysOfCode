print("Welcome to the tip calculator!")
bill = float(input("What was the total bill: $"))
number_of_people = int(input("How many people to split the bill? "))
extra_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Calculate the new tip amount as a percentage of the bill
tip_amount = bill * (extra_tip / 100)

# Calculate the total bill including the tip
total_bill = bill + tip_amount

# Calculate the amount each person should pay
individual_share = total_bill / number_of_people
final_tip = round(individual_share, 2)

print(f"Each person should pay ${final_tip}")



