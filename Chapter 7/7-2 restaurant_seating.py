# Ask the user how many people are in their dinner group.
guests = input("How many will be sitting with you for dinner? ")
guests = int(guests)
# If they have more than 8 guests, they have to wait for a table.
if guests > 8:
    print("We're sorry, you will have to wait for a table.")
else:
    print(f"Great. We have a table for {guests}.")
