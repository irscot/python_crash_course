# Store User class in user.py
# Store Privileges and Admin classes in privileges_admin.py
# In this file create an Admin instance
from privileges_admin import Admin

kyuusei = Admin('kyuusei', 'sukotto', 'Persona 5 Royal', 'crimson')
kyuusei.describe_user()

kyuusei_privileges = [
    'can delete comments',
    'can mark comments as spoilers',
    'can ban users',
]

kyuusei.privileges.privileges = kyuusei_privileges

print(f"\nAdmin {kyuusei.first_name} has the following privileges")
kyuusei.privileges.show_privileges()
