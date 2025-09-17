# Make a dictionary containing 3 rivers in Japan and where they are.

rivers = {'kitagawa': 'kansai',
          'teshiogawa': 'hokkaido',
          'kujigawa': 'kanto'}


# Use a loop to print a sentence about each river and their location.
for river_name, river_location in rivers.items():
    print(f"The {river_name.title()} river is in {river_location.title()}.")

# Use a loop to print the river's names.
print("\nThe following is a list of rivers:")
for river_name in set(rivers.keys()):
    print(river_name.title())

# Use a loop to print the river's locations.
print("\nThe following are the location of those rivers:")
for river_location in set(rivers.values()):
    print(river_location.title())

