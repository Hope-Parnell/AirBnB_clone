#!/usr/bin/python3

from models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, *args, **kwargs):
        #will be the Place.id
        self.place_id = ""
        #will be the User.id
        self.user_id = ""
        self.text = ""
        super().__init__(*args, **kwargs)
