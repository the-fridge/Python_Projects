''' You need to install geopy first using
pip3 install geopy
'''
from geopy.geocoders import Nominatim
# This project gives you the location of the city you
# entered along with its latitude and longitude
'''
For this program to work an internet connection is required
as Nominatim fetches the location from its server.
'''
city = input("Enter City: ")
location = Nominatim().geocode(city)  # Fetches the location
print(location)
print("Latitude  : %s" % location.latitude)
print("Longitude : %s" % location.longitude)
