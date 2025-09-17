class Restaurant:
    """Describes a restaurant and what they serve."""

    # Store (self, restaurant_name, cuisine_type) arguments in the __init__() method.
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type."""
        # Let's capitalize the name of the restaurant.
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

        # 1 - Add an attribute called number_served with a default value of 0.
        self.number_served = 0

    def describe_restaurant(self):
        """Prints message about the name and food served at a restaurant."""
        message = f"{self.restaurant_name} is a good place to get {self.cuisine_type}."
        print(f"\n{message}")

    def open_restaurant(self):
        """Prints a message that the restaurant is open"""
        message = f"Welcome to {self.restaurant_name}! We are now open!"
        print(f"\n{message}")

    # 4 - Change the default value and print it again with a method.
    # Add a method called set_number_served() that lets you set the number served.
    # Don't forget to put number_served as an attribute!
    def set_number_served(self, number_served):
        """Lets user set number of customers served"""
        self.number_served = number_served

    # 5 - Add a method called increment_number_served() that lets you increment the number served.
    # Put more_customers or something else descriptive that shows you are adding more customers.
    def increment_number_served(self, more_customers):
        self.number_served += more_customers