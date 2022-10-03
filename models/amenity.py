#!/usr/bin/python3
"""Amenity module  """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class Amenity """
    name = ""

     def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(self, *args, **kwargs)
