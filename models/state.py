#!/usr/bin/python3
"""Module contains the State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class definition"""
    def __init__(self, *args, **kwargs):
        """initilizes a State"""
        self.name = ""
        super().__init__(*args, **kwargs)
