#!/usr/bin/python3
"""define the storage"""

import json


class FileStorage():
    """class that stores objects in JSON strings
    file_path (str): path of the JSON file
    objects (dict): stores all objects by class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """set a new object in __objects dictionary,
        with key <obj class name>.id"""
        name = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[name] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(self.__objects, f, default=str)

    def reload(self):
        """deserialize the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
        except Exception:
            return
