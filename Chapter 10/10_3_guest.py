# Write a program that prompts the user for their name.
name_please = input("What is your name? ")

# When they respond, write their name to a file called guest.txt.
filename = 'guest.txt'
with open(filename, 'w') as file_object:
    file_object.write(f"Greetings, {name_please.title()}.")
