# Make a class called Restaurant.

class Restaurant:
    """Describes a restaurant and what they serve."""
    # Store (self, restaurant_name, cuisine_type) arguments in the __init__() method.
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type."""
        # Let's capitalize the name of the restaurant.
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints message about the name and food served at a restaurant."""
        message = f"{self.restaurant_name} is a good plae to get {self.cuisine_type}."
        print(f"\n{message}")

    def open_restaurant(self):
        """Prints a message that the restaurant is open"""
        message = f"Welcome to {self.restaurant_name}! We are now open!"
        print(f"\n{message}")

# Make an instance called restaurant from the Restaurant class.
# Print the two attributes individually.

restaurant = Restaurant('ichiraku ramen', 'ramen')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Call both methods.

restaurant.describe_restaurant()
restaurant.open_restaurant()

