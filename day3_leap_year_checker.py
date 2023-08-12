year = int(input("Enter any year to check if it's a Leap year or not: "))
# Check if year is evenly divisible by 4, i.e. without a remainder
if year % 4 == 0:
    # Next check if the above is true
    if year % 100 == 0:
        # If above is true, next check
        if year % 400 == 0:
            print(f"{year} is a Leap year.")
            # Not true, do this
        else:
            print(f" {year} is not a Leap year.")
            # If year isn't divisible by 100, do this
    else:
        print(f"{year} is a Leap year.")
        # If not divisible by 4, do this
else:
    print(f"{year} is not a Leap year.")
