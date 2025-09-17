# Write a program that polls users about their dream vacation.

name_prompt = "What is your name? "
location_prompt = "Where would you like to go? "
continue_prompt = "Anymore poll takers? (y/n) "

dream_vacations = {}

while True:
    # Ask user their name and where would they like to go.
    name = input(name_prompt)
    dream_vacation = input(location_prompt)

    # Put the response in the dictionary.
    dream_vacations[name] = dream_vacation

    # Ask if anyone else wants to take the poll.
    anyone_else = input(continue_prompt)
    if anyone_else != 'y':
        break

# Show survey's results (out of the while loop!)
print("Here are the results!")
# Put name as the key and dream vacation as the value
for name, dream_vacation in dream_vacations.items():
    print(f"\n{dream_vacation.title()} sounds like a fun place, {name.title()}.")
