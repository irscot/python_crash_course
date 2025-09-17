# Write a function called city_country()
# that takes in the name of a city and a country.


def city_country(city_name, country_name):
    """Return a string like 'Hiroshima, Japan'."""
    return f"{city_name.title()}, {country_name.title()}"

    # Past code I tried:
    # print("\nPlease tell me a city, and it's country below.")
    # city_name = input('give me a city: ')
    # country_name = input('give me the country it corresponds to: ')
    # city_country_names = {'City': city_name.title(), 'Country': country_name.title()}
    # return city_country_names


city = city_country('hiroshima', 'japan')
print(city)
