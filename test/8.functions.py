# Chapter 8 : functions (java, c# - method)

# declaring, defining function here
def greet_user():
    print("Hello!")


greet_user()  # calling the function, actual execution happens
greet_user()
greet_user()
greet_user()


# 8.3.
def make_shirt(size, message):
    print(f"the size {size.upper()} has a message '{message.title()}'.")


make_shirt('s', 'queen')
make_shirt('m', 'perfert')
make_shirt('l', 'love')


# 8.4.
def make_shirt(size="L", message="I love Python"):
    print(f"The size {size.upper()} has a message '{message}'.")


make_shirt()
make_shirt("m")
make_shirt("s", "blabla")


# 8.5.

def describe_city(city, country="georgia"):
    print(f"{city.title()} is in {country.title()}.")


describe_city('tbilisi')
describe_city('kutaisi')
describe_city('paris', 'france')


# 8.6.

def city_country(city, country):
    country_city = f"{city} {country}"
    return country_city.title()


place = city_country('Paris', 'France')
print(place)


def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

person = get_formatted_name('Andro', 'Jvania')
print(person)

person = get_formatted_name('emily', 'campolo', 'anastacia')
print(person)

# 8.7.

def make_album(artist_name, album_title):
    album = {'Artist': artist_name, 'Album': album_title}
    return album

album1 = make_album("Muse", "Resistance")
album2 = make_album("Queen", "News OF The World")
album3 = make_album("Radiohead", "The bend")

print(album1, album2, album3)
print(f"{album1['Artist']} has a great album called '{album1['Album']}'.")
print(f"{album2['Artist']} has a great album called '{album2['Album']}'.")
print(f"{album3['Artist']} has a great album called '{album3['Album']}'.")




def make_album(artist_name, album_title, num_tracks=None):
    album = {'Artist': artist_name, 'Album': album_title, 'Tracks': num_tracks}
    return album

album1 = make_album("Muse", "Resistance")
album2 = make_album("Queen", "News OF The World")
album3 = make_album("Radiohead", "The bend", 6)

print(album1, album2, album3)
print(f"{album1['Artist']} has a great album called '{album1['Album']}'.")
print(f"{album2['Artist']} has a great album called '{album2['Album']}'.")
print(f"{album3['Artist']} has a great album called '{album3['Album']}' with {album3['Tracks']} tracks in it.")


