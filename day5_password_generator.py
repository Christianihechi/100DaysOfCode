import random
print("PYPassword Generator 🔐🗝️")  # By Christian Ihechi
letters = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F',
           'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K',
           'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q',
           'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V',
           'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

n_letters = int(input("How many letters would you like in your password: "))
n_numbers = int(input("How many numbers: "))
n_symbols = int(input("How many symbols would you like: "))


password = ''

for i in range(n_letters):
    password += random.choice(letters)

for i in range(n_numbers):
    password += random.choice(numbers)

for i in range(n_symbols):
    password += random.choice(symbols)

ran_pass = ''.join(random.sample(password, len(password)))

print(f"Here's your generated password: {ran_pass}")
