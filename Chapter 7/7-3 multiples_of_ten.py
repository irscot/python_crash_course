# Ask user for a number.
number = input("Give me a number. Any number at all: ")
number = int(number)

if number % 10 == 0:
    print("This number is a multiple of 10.")
else:
    print("This number is not a multiple of 10.")