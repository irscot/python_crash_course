# Write a program that prompts for two numbers.
# Use a try-except-else chain for this program.
try:
    print("Give me two numbers and I will add them")
    first_num = input("What is your first number? ")
    first_num = int(first_num)

    second_num = input("Second number? ")
    second_num = int(second_num)

    # Catch the ValueError if either input value is not a number.
    # Print an error message.
except ValueError:
    print("Sorry I need to integers for this to work.")

# Add them together and print the result
else:
    sum = first_num + second_num
    print(f"{first_num} and {second_num} added together equals {sum}.")
