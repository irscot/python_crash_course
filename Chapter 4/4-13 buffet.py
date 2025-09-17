# Tuples are list that can't be changed.
# You can overwrite the original with a new one with the same name. Example at line 24.

# Buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
buffet_foods = ('rice', 'fish', 'beef', 'stir fried vegetables', 'ice cream')

# Use a for loop to print each food the restaurant offers.
print("Here are the foods served at this buffet restaurant:")
for buffet_food in buffet_foods:
    print(f"-{buffet_food}")

# The restaurant has changed the menu. Two items have been changed.
# Add a line that rewrites the tuple.
buffet_foods = ('fried rice', 'fish', 'beef', 'stir fried vegetables', 'pudding')

# Use a for loop to print the revised menu.
print("\nHere is the revised menu:")
for buffet_food in buffet_foods:
    print(f"-{buffet_food}")

# Try to modify the list and make sure that Python rejects the change.
# I'll try changing rice to udon.
buffet_foods[0] = 'udon'
print(buffet_foods)



