# Make a dictionary with 3 cities.

# Set the key to a city and nest a dictionary with info on that city.
cities = []
city = {'name': 'osaka',
        'population': 19_059_856,
        'fact': 'has a bunch of delicious food',
        'location': 'japan',
        }
cities.append(city)

city = {'name': 'katy',
        'population': 29_049,
        'fact': 'has a kinokuniya bookstore',
        'location': 'texas',
        }
cities.append(city)

city = {'name': 'new york city',
        'population': 8_177_020,
        'fact': 'has gogo curry',
        'location': 'new york',
        }
cities.append(city)

for city in cities:
    print(f"\nHere is some info about {city['name'].title()}:")
    for key, value in city.items():
        print(f"{key.title()}: {value}")
