# need to import choice from random to randomly select numbers or letters
from random import choice

# Make a list or tuple with a series of 10 numbers and five letters
lottery_code = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
                'a', 'b', 'c', 'd', 'e']

# Make an empty list for winning lottery ticket
won = []
print("The winner is...")

# randomly select four numbers or letters from the list
while len(won) < 4:
    lot = choice(lottery_code)

    # If the lot hasn't been taken yet add the lot to won.
    if lot not in won:
        print(f"{lot}!")
        won.append(lot)

print(f"The person with lot {won} come down and claim your prize!")
