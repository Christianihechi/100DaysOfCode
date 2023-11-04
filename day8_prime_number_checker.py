import math


def prime_checker(number):
    if number <= 1:
        print(f"{number} is not a Prime number")
        return

    square_root = math.isqrt(number)
    is_prime = True  # Assume it's prime until proven otherwise

    # Check divisibility by 2
    if number > 2 and number % 2 == 0:
        is_prime = False

    # Check divisibility by odd numbers from 3 to square_root (inclusive)
    for num in range(3, square_root + 1, 2):
        if number % num == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a Prime number")
    else:
        print(f"{number} is not a Prime number")


print("Prime Number Checker.")
n = int(input("Enter a number: "))
prime_checker(number=n)
