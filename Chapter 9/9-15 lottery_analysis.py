from random import choice


def you_won(chances):
    """Return winning ticket from chances."""
    winner = []

    # Use a loop to see your chances of winning at the lottery from 9-14 lottery.py.
    while len(winner) < 4:
        pulled_lot = choice(chances)

        # If the lot hasn't been taken yet add the lot to won.
        if pulled_lot not in winner:
            winner.append(pulled_lot)

    return winner


def lot_checker(lot_pulled, winner):
    """Checks if the lot pulled is a winner or not."""
    # Check all elements in lot_pulled.
    # If they are not winners, return false.
    for element in lot_pulled:
        if element not in winner:
            return False

    # Have to have winning lot.
    return True


# Make a function that pulls out a random ticket.

def random_lot(chances):
    """Return random lot form set of chances"""
    lot = []

    while len(lot) < 4:
        pulled_lot = choice(chances)

        # Only add the lot to the list if it hasn't been taken yet.
        if pulled_lot not in lot:
            lot.append(pulled_lot)

    return lot


chances = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
           'a', 'b', 'c', 'd', 'e']
winner = you_won(chances)

pulls = 0
won = False

max_tries = 1_000_000_000

while not won:
    new_ticket = random_lot(chances)
    won = lot_checker(new_ticket, winner)
    pulls += 1
    if pulls >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winner}")
    print(f"It only took {pulls} tries to win!")
else:
    print(f"You've pulled {pulls} times in this lottery without winning. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {won}")
