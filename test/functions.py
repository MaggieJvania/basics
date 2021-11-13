# Chapter 8 : functions (java, c# - method)

# declaring, defining function here
def greet_user():
    print("Hello!")


def make_shirt(size, message):
    print(f"the size {size.upper()} has a message '{message.title()}'.")


def make_shirt(size="L", message="I love Python"):
    print(f"The size {size.upper()} has a message '{message}'.")


def describe_city(city, country="georgia"):
        print(f"{city.title()} is in {country.title()}.")


def city_country(city, country):
    country_city = f"{city} {country}"
    return country_city.title()


def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


def make_album(artist_name, album_title):
    album = {'Artist': artist_name, 'Album': album_title}
    return album


def make_album(artist_name, album_title, num_tracks=None):
    album = {'Artist': artist_name, 'Album': album_title, 'Tracks': num_tracks}
    return album




