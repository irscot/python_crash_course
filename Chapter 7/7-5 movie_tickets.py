# Write a loop with in an input that asks for the person's age
# and tell them the cost of their ticket.

prompt = "\nWelcome to the theater!"
prompt += "\nBefore you purchase a ticket, how old are you? "

active = True

while active:
    # Brought input method into the while loop, so user can put in more ages.
    age = input(prompt)
    age = int(age)

    # Wrote an if-elif-else chain that tells the user
    # what the price of their ticket will be
    # depending on their age.
    if age < 3:
        print(f"You are {age}, your ticket is free.")
    elif age < 12:
        print(f"You are {age}, your ticket is $10.")
    else:
        print(f"You are {age}, your ticket is $15.")
