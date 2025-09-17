# Make a list of 5 usernames including the name admin.
user_names = ['haixis', 'zay0', 'kyu00', 'rei', 'admin']

# Run a loop greeting all users.
for user_name in user_names:
    # If the username is admin write a special message to them.
    if user_name == 'admin':
        print("Hey there, admin! Want a status report?")
    # If not the admin, give a similar message to each username.
    else:
        print(f"Hey, {user_name.title()}! Welcome back!")

