countries = ("France", "Austria", "Canada", "Germany", "Spain")

print("The countries are:", countries)

country_removed = input("Choose a country to see its index:")

while(country_removed.title() not in countries):
    country_removed = input("Invalid input!\nPlease insert a country from the list:")

print("The index of {0} is {1}".format(country_removed, countries.index(country_removed.title())))
