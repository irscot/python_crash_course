# Write a while-loop that asks people why they like programming.
filename = 'why_we_like_programming.txt'

reasons = []

while True:
    reason = input("\nWhy do you like programming? ")
    # Have to add each reason to the list.
    reasons.append(reason)

    # Have to have a way to stop the program.
    continue_asking = input("Anyone else have a reason? (y/n) ")

    if continue_asking != 'y':
        break

# Every time someone enters a reason, add that reason to file that stores them.
with open(filename, 'a') as file_object:
    for reason in reasons:
        file_object.write(f"{reason}\n")
