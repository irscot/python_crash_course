# make sandwich_orders list and fill it with various sandwiches.
# Nah let's go with ramen!
ramen_orders = ['pork cutlet', 'chicken', 'vegetable', 'shoyu']
finished_orders = []

# Loop through the list and print a message for each order.
while ramen_orders:
    order = ramen_orders.pop()

    print(f"One order of {order} ramen comin' right up!")
    finished_orders.append(order)

print("\nHere's your: ")
for finished_order in finished_orders:
    print(f"{finished_order} ramen")