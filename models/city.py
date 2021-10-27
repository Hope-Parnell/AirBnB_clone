#!/usr/bin/python3

from models.base_model import BaseModel

class City(BaseModel):
    def __init__(self, *args, **kwargs):
        #will be state.id
        self.state_id = ""
        self.name = ""
        super().__init__(*args, **kwargs)
