#!/usr/bin/python3
"""Module contains Reveiw class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class definition"""
    #  will be the Place.id
    place_id = ""
    #  will be the User.id
    user_id = ""
    text = ""
