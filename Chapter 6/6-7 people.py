# Start out with program from 6-1 person.py.
# Use a dictionary to store info about a person.
# Make a dictionary about two different people.

people = {
    'conan': {'first_name': 'コナン',
              'last_name': '江戸川',
              'age': 7,
              'city': '米花町'},

    'rei': {'first_name': 'Rei',
            'last_name': 'Kiriyama',
            'age': 19,
            'city': '六月町'},
}

# Print each piece of info in your dictionary.

for person, person_info in people.items():
    full_name = f"{person_info['first_name']} {person_info['last_name']}"
    age = person_info['age']
    city = person_info['city']
    print(f"\nFull name: {full_name.title()}")
    print(f"Age: {age}")
    print(f"City: {city.title()}")
