#!/usr/bin/python3
"""Base model for Holberton AirBnB project"""
import uuid
import json
import datetime
import models


class BaseModel:
    """created Class for BaseModel"""
    def __init__(self) -> None:
        """public instance attributes for BaseModel"""
        time_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()

    def __str__(self) -> str:
        """String override for BaseModel"""
        return "[{}] ({}) {}".format(__name__, self.id, self.__dict__)

    def save(self):
        """updates (updated_at attribute)to current time"""
        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        """returns a dictionary of Class instance"""
        self.__dict__[__class__] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat
        self.__dict__["updated_at"] = self.updated_at.isoformat
        return self.__dict__

    
