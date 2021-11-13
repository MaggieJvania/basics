# module is a python file
from functions import *


greet_user()  # calling the function, actual execution happens
greet_user()
greet_user()
greet_user()


make_shirt('s', 'queen')
make_shirt('m', 'perfert')
make_shirt('l', 'love')


make_shirt()
make_shirt("m")
make_shirt("s", "blabla")


describe_city('tbilisi')
describe_city('kutaisi')
describe_city('paris', 'france')


place = city_country('Paris', 'France')
print(place)


person = get_formatted_name('Andro', 'Jvania')
print(person)

person = get_formatted_name('emily', 'campolo', 'anastacia')
print(person)


album1 = make_album("Muse", "Resistance")
album2 = make_album("Queen", "News OF The World")
album3 = make_album("Radiohead", "The bend")

print(album1, album2, album3)
print(f"{album1['Artist']} has a great album called '{album1['Album']}'.")
print(f"{album2['Artist']} has a great album called '{album2['Album']}'.")
print(f"{album3['Artist']} has a great album called '{album3['Album']}'.")



album1 = make_album("Muse", "Resistance")
album2 = make_album("Queen", "News OF The World")
album3 = make_album("Radiohead", "The bend", 6)

print(album1, album2, album3)
print(f"{album1['Artist']} has a great album called '{album1['Album']}'.")
print(f"{album2['Artist']} has a great album called '{album2['Album']}'.")
print(f"{album3['Artist']} has a great album called '{album3['Album']}' with {album3['Tracks']} tracks in it.")


