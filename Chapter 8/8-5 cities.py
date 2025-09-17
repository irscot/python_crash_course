# Write a function that describes a city
# with a name and its country.

# Give the country parameter a default value. Of course, I'm going with Japan!
def describe_city(name, country='japan'):
    print(f"The city called {name.title()} is in {country.title()}.")


# Call function 3 times for 3 different cities in Japan.
describe_city('hiroshima')
describe_city('akihabara')
describe_city('yokohama')

# Call the function with a different country.
describe_city('louisville', country='america')
