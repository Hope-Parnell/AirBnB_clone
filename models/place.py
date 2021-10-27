#!/usr/bin/python3

from models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, *args, **kwargs):
        #will be city.id
        self.city_id = ""
        #will later be user.id
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        #list of strings. will be the list of Amenity.ids
        self.amenity_ids = []
        super().__init__(*args, **kwargs)
