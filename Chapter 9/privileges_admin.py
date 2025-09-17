# Need to import class User from user.py
from user import User

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