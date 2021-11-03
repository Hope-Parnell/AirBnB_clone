#!/usr/bin/python3
"""Module contains the Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class definition"""
    #  will be city.id
    city_id = ""
    #  will later be user.id
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    #  list of strings. will be the list of Amenity.ids
    amenity_ids = []
