# Start with the class form 9-1 restaurant.py
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
        message = f"{self.restaurant_name} is a good place to get {self.cuisine_type}."
        print(f"\n{message}")

    def open_restaurant(self):
        """Prints a message that the restaurant is open"""
        message = f"Welcome to {self.restaurant_name}! We are now open!"
        print(f"\n{message}")


# Create three different instances from the class. Call describe restaurant() for each.
restaurant_1 = Restaurant('ichiraku ramen', 'ramen')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant('krusty krab', 'burgers')
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant('chef emiya kitchen', 'hambuger steak')
restaurant_3.describe_restaurant()