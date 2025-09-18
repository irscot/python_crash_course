# Start with 9-8
# Store classes User, Privileges, and Admin in module admin_checker.
# import admin_checker.
from admin_checker import Admin

# Make an admin instance and call describe_user.
isiah = Admin('isiah', 'isaiah', 'persona 3', 'midnight blue')
isiah.describe_user()

# Call show_privileges.
isiah_privileges = ['can delete comments',
                   'can mark comments as spoilers',
                   'can ban users']

isiah.privileges.privileges = isiah_privileges

print(f"Admin {isiah.first_name} has the following privileges: ")

isiah.privileges.show_privileges()
