# Make a list of three kinds of pizzas. Use a for loop to print name of each pizza

pizzas = ['cheese', 'pepperoni', 'pineapple']

# Copy the pizza list into friends_pizzas
friends_pizzas = pizzas[:]

# Add a new pizza to pizzas
pizzas.append('extra cheese')

# Add a new pizza to friends_pizzas
friends_pizzas.append('salsa verde')



#Make a sentence with each type of pizza
print(f"\nMy favorite pizzas are:")
for pizza in pizzas:
    print(f"{pizza}")

print(f"\nMy friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(f"{pizza}")

#Make a sentence outside loop. NOTE: Make sure not to indent it!

print("\nWe love pizza!")