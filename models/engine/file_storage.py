#!/usr/bin/python3


""" define the storage"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """class that stores objects in JSON strings
    file_path (str): path of the JSON file
    objects (dict): stores all objects by class"""

    __file_path = 'file.json'
    __objects = {}
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """set a new object in __objects dictionary,
        with key <obj class name>.id"""
        i = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[i] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        save_dict = {}
        for i, value in FileStorage.__objects.items():
            value_dict = value.to_dict()
            save_dict[i] = value_dict
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(save_dict, f)