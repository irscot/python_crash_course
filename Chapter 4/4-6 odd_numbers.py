# Use the third argument in range() to make a "list" of odd numbers from 1 to 20.
odd_numbers = list(range(1,21,2))
print(odd_numbers)

# Use a for loop to print each number.
# Need to change up the name a bit. It'll just print out odd_numbers above.
# This will be a for loop so I went with odd_numbers_for.
odd_numbers_for = []

for value in range(1,21,2):
    odd_numbers_for.append(value)

print(odd_numbers_for)

