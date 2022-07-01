#!usr/bin/python3
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
    classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amentiy",
        "Review"}


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
        save_dict = {name: value.to_dict() for name,
                    value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(save_dict, f)

    def reload(self):
        """deserialize the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                FileStorage.__objects = {}
                for name, value in data.items():
                    obj = BaseModel(**value)
                    FileStorage.__objects[name] = obj
        except FileNotFoundError:
            return

    def show(self, args):
        """prints the string representaiton of an string"""
        arg = pase(args)
        objdict = storage.all()
        if len(arg) == 0:
            print("** class doesn't exist **")
        elif arg[0] not in HBNBcommand.__class__:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id  mising **")
        elif "{}.{}"format(arg[0], arg[1]) not in objdict:
            print("** no instance found **")

    def do_destroy(self, args):
        """deletes aninstance based on the class name and id"""
        arg = parse(args)
        objdict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBcommand.__class__:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}"format(arg[0], arg[1]) not in objdict:
            print("** no instance found **")

    def all(self, args):
        """prints allstring representation of all instances
        based or not on the class name"""
        arg = parse(args)
        objdict = storage.all()
        if len(arg) == 0:
            print("** class name doesn't exist **")
