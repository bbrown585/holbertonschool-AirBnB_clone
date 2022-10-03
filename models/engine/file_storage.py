#!/usr/bin/python3
"""Adds Class FileStorage to Holberton AirBnB project"""
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json


class_keys = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
              "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """
    Stores objects as json strings
    and converts them back into python objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all object instances"""
        return self.__objects

    def new(self, obj):
        """adds all """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """saves object instance in json file"""
        my_dict = {}
        for key in self.__objects:
            my_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(my_dict, f)

    def reload(self):
        """converts a json file into a python object"""
        try:
            with open(self.__file_path, 'r') as f:
                new_dict = json.load(f)
            for key in new_dict:
                class_name = new_dict[key]["__class__"]
                self.__objects[key] = class_keys[class_name](**new_dict[key])
        except FileNotFoundError:
            pass
