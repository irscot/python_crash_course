# Make a list of numbers from 1 to 1 million.
numbers = []

# Use 1_000_001 so, it doesn't stop at 999_999 when ran.
for value in range(1, 1_000_001):
    numbers.append(value)

print(numbers)
