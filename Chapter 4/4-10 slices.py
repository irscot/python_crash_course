# Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following.

# I'll make a new list with japanese foods.
japanese_foods = ['ramen', 'gyudon', 'takoyaki', 'curry', 'sushi']
print(f"Here is the list of Japanese foods I want to try: \n{japanese_foods}")

# Print the message The first three items in the list are:
print("\nThe first three items in the list are:")

# Then use a slice to print the first three items from that program’s list.
print(f"{japanese_foods[:3]}")

# Print the message Three items from the middle of the list are:
print("\nThree items from the middle of the list are:")

#Use a slice to print three items from the middle of the list.
print(f"{japanese_foods[1:4]}")

# Print the last three items from the list are:
print("\nThe last three items from the list are:")

# Use a slice to print the last three items in the list.
print(f'{japanese_foods[2:]}')
