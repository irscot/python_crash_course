# Make a dictionary of three people's favorite places for each.

# Ask them what is there favorite places.
names = ['naruto', 'rei', 'mizuto']
for name in names:
    print(f"Hey {name.title()}, what are your favorite places to go?")

# Make a separate dictionary for each person.
favorite_places = {'naruto': {'ichiraku ramen', 'training field', 'greenhouse'},
                   'rei': {'home', "kawamoto house", 'shogi research circle'},
                   'mizuto': {'home', 'library', 'bookstore'},
                   }
# Loop through each dictionary
# and print message about their favorite places along with their name.
for name, places in favorite_places.items():
    print(f"\n{name.title()} likes to hang out at:")
    for place in places:
        print(f"\t{place.title()}")