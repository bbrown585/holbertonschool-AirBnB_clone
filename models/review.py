#!/usr/bin/python3
"""adds Reviw class to Holberton AirBnB project"""
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
