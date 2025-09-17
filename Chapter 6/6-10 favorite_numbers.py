# Modify 6-2 favorite_numbers.py so everyone can have more than one number.
# Use a dictionary to store people's favorite numbers.
# Think of 5 names and use them as keys. Think of a number for each name.

favorite_numbers = {'isiah': [0, 29],
                    'nigel': [1, 10],
                    'abigail': [5, 31],
                    'nomura': [13, 4],
                    'david': [3, 6],
                    }

# Print each name with their favorite number.
number = favorite_numbers['isiah']
print(f"Isiah's favorite numbers are {number}.")

number = favorite_numbers['nigel']
print(f"Nigel's favorite numbers are {number}.")

number = favorite_numbers['abigail']
print(f"Abigail's favorite numbers are {number}.")

number = favorite_numbers['nomura']
print(f"Nomura's favorite numbers are {number}.")

number = favorite_numbers['david']
print(f"David's favorite numbers are {number}.")

# Let's try this in a loop.
print("\nLet's try a for loop!")
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes these numbers:")
    for number in numbers:
        print(f"\t{number}")