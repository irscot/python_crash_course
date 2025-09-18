# Make a list of 5 usernames called current users.
current_users = ['isiah', 'detco', 'kiri', 'slyfox', 'admin']

# Make a list of called new_users with new usernames.
# Make sure one is from the current_users list.
new_users = ['vegetareviews69', 'isiah', 'm0nke', 'giggUK', 'based日本語上手']

# Make sure usernames are case-insensitive.
current_users_lower = [user.lower() for user in current_users]

# Loop through new_users list if each new username is used.
for new_user in new_users:
    # If new user has the same username as a current user tell them the name is taken.
    if new_user.lower() in current_users_lower:
        print(f"The username {new_user} has been taken. Please find another one.")
    # If new user has a different username then tell them the name is available.
    else:
        print(f"The username {new_user} is available.")




