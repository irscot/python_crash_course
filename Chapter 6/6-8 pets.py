# Make several dictionaries for different pets.
# Include kind of animal and the owner's name in each.
pet_list = ['sparky', 'snow']

pets = {
        'sparky': {'animal': 'dog',
                   'name': 'sparky',
                   'owner': 'jackson'},

        'snow': {'animal': 'cat',
                 'name': 'snow',
                 'owner': 'carly'},
        }

for pets, pet_info in pets.items():
    animal = pet_info['animal']
    name = pet_info['name']
    owner = pet_info['owner']
    print(f"The owner of {name.title()} the {animal} is {owner.title()}.")

# Revised to actually make use of the list.

print("\nRevised Version")

# Made an empty list.
pets = []

# Created dictionaries within a dictionary for each pet.
# Added each pet dictionary to the list with the append method.
pet = {
        'animal': 'dog',
        'name': 'sparky',
        'owner': 'jackson',
        }
pets.append(pet)

pet = {
        'animal': 'cat',
        'name': 'snow',
        'owner': 'carly',
        }
pets.append(pet)

# Wrote a for loop while assigning callable variables to print a message.
for pet in pets:
    print(f"Here's a list of things I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")
