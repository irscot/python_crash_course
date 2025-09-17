# Make a class called User
class User:
    """Holds info of users"""

    # Create attributes for the users
    def __init__(self, first_name, last_name, fave_game, fave_color):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.fave_game = fave_game.title()
        self.fave_color = fave_color

    # Make a method called describe_user() that prints user's info.
    def describe_user(self):
        """Provides info on user"""
        info = f"Name: {self.first_name} {self.last_name}" \
               f"\nFavorite game: {self.fave_game}" \
               f"\nFavorite color: {self.fave_color}"

        print(info)

    # Make a method greeting the user.
    def greet_user(self):
        """Say hello to the user"""
        greeting = f"Hi there {self.first_name}!"

        print(greeting)


# Create an instance and call methods
isiah_scott = User('isiah', 'scott', 'kingdom hearts', 'scarlet')
isiah_scott.describe_user()
isiah_scott.greet_user()
