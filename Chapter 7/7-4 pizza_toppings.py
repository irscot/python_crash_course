# Write a loop that prompts the user to enter pizza toppings until they enter quit.

# Made an empty list for pizza toppings.
pizza_toppings = []

# Set up a prompt to ask user about a pizza topping.
prompt = "Tell me a pizza topping and I'll add it to the list. "
prompt += "\nEnter 'quit' when you are done: "

# Made a while loop
while True:
    # Brought in the input method, so user can add more toppings.
    pizza_topping = input(prompt)

    # If the user wants to quit the program they enter quit.
    if pizza_topping == 'quit':
        break
    # The else here is used when the user doesn't want to quit the program.
    # It adds the pizza topping to the pizza toppings list
    # and prints the list.
    else:
        print(f"\nI'll add {pizza_topping} to the list.")
        pizza_toppings.append(pizza_topping)
        print(list(pizza_toppings))
