# Make a list of numbers from 1 to 1 million.
numbers = []

# Use 1_000_001 so, it doesn't stop at 999_999 when ran.
for value in range(1, 1_000_001):
    numbers.append(value)

print(numbers)


# Use min() and max() to check the first and last numbers are one and one million.
print("\nHere is the min:")
print(min(numbers))

print("\nHere is the max:")
print(max(numbers))


# Use sum() to see what number comes from the sum of up to 1 million.
print("\nHere is the sum of numbers one to one million:")
print(sum(numbers))