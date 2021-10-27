#!/usr/bin/python3
"""Module contains the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for users"""
    def __init__(self, *args, **kwargs):
        """initilizes a user"""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(*args, **kwargs)
