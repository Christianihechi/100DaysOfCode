print("Welcome To Python Pizza Deliveries!\n")
pizza_size = input("What size of Pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want Pepperoni? Y or N: ")
add_cheese = input("Do you want Cheese? Y or N: ")

cost = 0

if pizza_size == 'S':
    cost += 15
elif pizza_size == 'M':
    cost += 20
elif pizza_size == 'L':
    cost += 25

if add_pepperoni == 'Y':
    if pizza_size == 'S' or pizza_size == 'M':
        cost += 2
    else:
        cost += 3

if add_cheese == 'Y':
    cost += 1

print(f"Your final bill is: ${cost}")
