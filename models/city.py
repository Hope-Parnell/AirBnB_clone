#!/usr/bin/python3
"""Module contains City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Is the City class"""
    def __init__(self, *args, **kwargs):
        """initilizes the City"""
        #  will be state.id
        self.state_id = ""
        self.name = ""
        super().__init__(*args, **kwargs)
