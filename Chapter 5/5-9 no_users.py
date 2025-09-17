# Add an if test to 5-8 to check if the list is empty.

# Remove usernames from list.
user_names = []

# Run a loop greeting all users.
for user_name in user_names:
    # If the username is admin write a special message to them.
    if user_name == 'admin':
        print("Hey there, admin! Want a status report?")
    # If not the admin, give a similar message to each username.
    else:
        print(f"Hey, {user_name.title()}! Welcome back!")

# Use an if statement to check if list is empty.
if user_names == []:
    print("Quick! We need to find some users!")