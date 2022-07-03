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


if __name__ == '__main__':
    HBNBCommand().cmdloop()