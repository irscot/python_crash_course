# Take 7-8 list and make sure onion shows up in the list three times.

ramen_orders = ['pork cutlet', 'onion', 'chicken', 'onion', 'vegetable', 'shoyu', 'onion']
print(ramen_orders)

# Add a message saying we are out of onion.
print("\nWe are out of onion ramen.")

# Remove all instances of ramen from ramen_orders list.
while 'onion' in ramen_orders:
    ramen_orders.remove('onion')

print(ramen_orders)
