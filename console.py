#!/usr/bin/python3

from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import cmd
import sys

"""command interpreter"""

my_dict = {'Amenity': Amenity, 'BaseModel': BaseModel, 'City': City,
           'Place': Place, 'Review': Review, 'State': State, 'User': User}


class HBNBCommand(cmd.Cmd):
    """class of prompt"""
    prompt = '(hbnb) '
    
    def do_quit(self, args):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, args):
        """ exit the program"""
        return True

    def emptyline(self):
        """dont do anything if theres an empty line"""
        pass
    
    def do_help(self, arg):
        return super().do_help(arg)

    def do_create(self, args):
        """ def create """
        arg = args.split(" ")
        if arg[0] is None or arg[0] == "":
            print("** class name missing **")
        elif arg[0] in my_dict:
            object = getattr(sys.modules[__name__], arg[0])
            inst = object()
            print(inst.id)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
