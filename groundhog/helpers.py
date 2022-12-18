from flask import redirect, session
from functools import wraps
from geopy.geocoders import Nominatim
import requests


def error(message, code=400):
    return redirect("/")


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/auth/login")
        return f(*args, **kwargs)

    return decorated_function


def get_geocode(address):
    geolocator = Nominatim(user_agent="groundhog")
    location = geolocator.geocode(address)
    return (location.latitude, location.longitude)


def get_coordinates(ip_address):
    response = requests.get(f"https://ipapi.co/{ip_address}/json/").json()

    if "error" not in response:
        latitude = response["latitude"]
        longitude = response["longitude"]
        return latitude, longitude
    else:
        latitude = 40.7943793
        longitude = -73.9719996
        return latitude, longitude
