#!/usr/bin/python3
"""Module contains Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class contains amentities"""
    def __init__(self, *args, **kwargs):
        """initilized amentities"""
        self.name = ""
        super().__init__(*args, **kwargs)
