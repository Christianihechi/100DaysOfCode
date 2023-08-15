row1 = ['📦', '📦', '📦']
row2 = ['📦', '📦', '📦']
row3 = ['📦', '📦', '📦']
treasure_map = [row1, row2, row3]
# print("   a\t\tb\t\tc")
print(f"{row1}\n{row2}\n{row3}")
position = input("Hint ! Type just two digits. The first number is the 'column' and second number is the 'row'.\n"
                 "Where do you want to put the treasure: ")

target_row = int(position[1]) - 1  # Row
target_column = int(position[0]) - 1  # Column

treasure_map[target_row][target_column] = 'X'

print(f"{row1}\n{row2}\n{row3}")
