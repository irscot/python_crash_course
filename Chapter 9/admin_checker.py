class User:
    """Holds info of users"""

    # Create attributes for the users
    # Add an attribute called login_attempts and set it to 0.
    def __init__(self, first_name, last_name, fave_game, fave_color):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.fave_game = fave_game.title()
        self.fave_color = fave_color
        self.login_attempts = 0

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

    # Make a method called increment_login that increments the value of login_attempts by 1.
    def increment_login_attempts(self):
        """Increments the count of login attempts by 1."""
        self.login_attempts += 1

    # Make a method that sets the amount of login attempts back to 0.
    def reset_login_attempts(self):
        """Resets login attempts to 0."""
        self.login_attempts = 0


# Add a sublcass Admin that inherits from the User class.
class Admin(User):
    """Gives Admin privileges to a user."""

    def __init__(self, first_name, last_name, fave_game, fave_color):
        """Initializes admin"""
        # Initialize attributes privileges
        super().__init__(first_name, last_name, fave_game, fave_color)
        # Add privileges as an attribute
        self.privileges = Privileges()


class Privileges:
    """Stores a list of privileges for admin user."""

    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    # Move the show_privileges method to this class.
    def show_privileges(self):
        """Shows list of privileges the admin has."""
        print("\nList of privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"○ {privilege}")
        else:
            print("This user does not have any admin privileges.")
