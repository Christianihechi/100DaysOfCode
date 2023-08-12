print("Welcome to the Roller Coaster Ride!")
height = int(input("Please, what is your height in cm: "))
bill = 0
if height >= 120:
    age = int(input("Thank you. \nPlease enter your age: "))
    if age < 12:
        bill += 5
    elif age <= 18:
        bill += 7
    elif age > 18:
        bill += 12
    if age == 45 or age <= 55:
        bill = 0

    need_photo = input("Do you want a photograph? Type Y or N: ")
    if need_photo.lower() == 'y':
        bill += 3
        print(f"Cost of ride is ${bill}.")
    else:
        print(f"Total cost of ride is ${bill}")
else:
    print("Sorry, you're not eligible to ride the roller coaster due to your height.")
