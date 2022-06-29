#!/usr/bin/python3
"""
define the storage
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """class that stores objects in JSON strings
    file_path (str): path of the JSON file
    objects (dict): stores all objects by class"""

    __file_path = 'file.json'
    __objects = {}
    class_dict = {
        "BaseModel": BaseModel}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """set a new object in __objects dictionary,
        with key <obj class name>.id"""
        name = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[name] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        save_dict = {}
        for name, value in FileStorage.__objects.items():
            value_dict = value.to_dict()
            save_dict[name] = value_dict
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(save_dict, f)

    def reload(self):
        """deserialize the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                dicts = json.load(f)
                FileStorage.__objects = {}
                for name, value in dicts.items():
                    obj = BaseModel(**value)
                    FileStorage.__objects[name] = obj
        except FileNotFoundError:
            return
