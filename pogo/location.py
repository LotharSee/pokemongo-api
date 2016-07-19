import logging
from geopy.geocoders import GoogleV3

import util

geolocator = GoogleV3()

def getLocation(search):
    loc = geolocator.geocode(search)
    return loc

def encodeLocation(loc):
    return (util.f2i(loc.latitude), util.f2i(loc.longitude), util.f2i(loc.altitude))


class Location(object):
    """Custom replacer to the geopy location object, preventing us to query it every time if we have the coordinates"""

    def __init__(self, latitude, longitude, altitude):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
