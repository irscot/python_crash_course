# Store numbers 1 - 9 in a list

ordinal_numbers = list(range(1, 10))

# Loop through list
print(ordinal_numbers)


# Use if-elif-else chain in a loop to print proper ordinal endings for each number.
# 1, 2 and 3 have different ending. Ex: 1st, 2nd, 3rd. So split those from the chain.
for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print("1st")
    elif ordinal_number == 2:
        print("2nd")
    elif ordinal_number == 3:
        print("3rd")
    # For the rest they all end in th. So use else.
    else:
        print(f"{ordinal_number}th")
