# Make a class called Die with on attribute called sides.
# Default sides to the number 6.
# If we are going to be randomly throwing a die we need from random import randint.
from random import randint

die_roll = randint(1, 6)


class Die:
    """Rolls a 6-sided die and tells what number it landed on."""

    # Initialize the die with method def __init__(self).
    # Default sides to the number 6.
    def __init__(self, sides=6):
        """Initializes the die."""
        self.sides = sides

    # Write a method called roll_die that prints a random number between 1 and 6.
    def roll_die(self):
        """"Return a number between 1 and the number of sides at random."""
        return randint(1, self.sides)


# Roll die 10 times
six_die = Die()

die_rolls = []

for random_number in range(10):
    die_roll = six_die.roll_die()
    die_rolls.append(die_roll)

print("10 rolls of a 6-sided die:")
print(die_rolls)

# Make a 10 sided die (default the sides to 10). Roll each 10 times.
# Rename instance to fit 10 sided die.
ten_die = Die(sides=10)

die_rolls = []

for random_number in range(10):
    die_roll = ten_die.roll_die()
    die_rolls.append(die_roll)

print("\n10 rolls of a 10-sided die:")
print(die_rolls)

# Make a 20 sided die (default the sides to 20). Roll each 10 times.
# Rename instance to fit 20 sided die.
twenty_die = Die(sides=20)

die_rolls = []

for random_number in range(10):
    die_roll = twenty_die.roll_die()
    die_rolls.append(die_roll)

print("\n10 rolls of a 20-sided die:")
print(die_rolls)
