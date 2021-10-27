#!/usr/bin/python3
"""Module contains Reveiw class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class definition"""
    def __init__(self, *args, **kwargs):
        """initilizes a review"""
        #  will be the Place.id
        self.place_id = ""
        #  will be the User.id
        self.user_id = ""
        self.text = ""
        super().__init__(*args, **kwargs)
