# Start with 9-8
# Store classes User, Privileges, and Admin in module admin_checker.
# import admin_checker.
from admin_checker import Admin

# Make an admin instance and call describe_user.
haixis = Admin('haixis', 'sixiah', 'persona 3', 'midnight blue')
haixis.describe_user()

# Call show_privileges.
haixis_privileges = ['can delete comments',
                   'can mark comments as spoilers',
                   'can ban users']

haixis.privileges.privileges = haixis_privileges

print(f"Admin {haixis.first_name} has the following privileges: ")
haixis.privileges.show_privileges()