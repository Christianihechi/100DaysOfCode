from caesar_cipher_char import characters


def caesar(text, shift, direction, final_text=''):
    if direction == 1:
        shift = shift  # No change needed for encoding
    elif direction == 2:
        shift = -shift  # Invert the shift direction for decoding

    for char in text:
        if char in characters:
            old_index = characters.index(char)
            new_index = (old_index + shift) % len(characters)
            result = characters[new_index]
            final_text += result
        else:
            final_text += char

    if direction == 1:
        print(f"Encoded text is:\n{final_text}")
    elif direction == 2:
        print(f"Decoded text is:\n{final_text}")


print("""
ADVANCED CAESAR CIPHER
""")

while True:
    print("Note:\n1. You can write letters(lower and upper case), numbers and symbols.\n"
          "2. Always use 'Shift numbers' that would be very hard to guess.\n")
    choice = int(input("Type 1 to 'encode(encrypt)' or 2 to 'decode(decrypt)':\n"))
    if choice > 2 or 1 > choice:
        print("Please enter one of the given options above.")
        continue
    t = input("Type your message:\n")
    s = int(input("Type the shift number:\n"))
    caesar(text=t, shift=s, direction=choice)
    redo = input("Would you like to continue? Yes or No: ").lower()
    if redo == 'yes':
        continue
    else:
        print("Thank you. Goodbye!")
        break
