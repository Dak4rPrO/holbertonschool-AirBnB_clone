#!/usr/bin/python3

""" Console 0.1 """
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

my_dict = {'Amenity': Amenity, 'BaseModel': BaseModel, 'City': City,
           'Place': Place, 'Review': Review, 'State': State, 'User': User}


class HBNBCommand(cmd.Cmd):
    """ Class that defines a small command interpreter """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, args):
        """ Exits the console """
        return True

    def emptyline(self):
        """ Nothing happens if there is an empty line """
        pass

    def do_help(self, arg):
        """ Command that display help messages """
        super().do_help(arg)

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

    def do_show(self, args):
        """prints the string representaiton of an string"""
        args.split(" ")
        objdict = storage.all()
        if len(args) == 0:
            print("** class doesn't exist **")
        elif args[0] not in HBNBCommand.__class__:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id  mising **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")

    def do_destroy(self, args):
        """deletes an instance based on the class name and id"""
        args.split(" ")
        objdict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__class__:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")

    def all(self, args):
        """prints allstring representation of all instances
        based or not on the class name"""
        args.split()
        objdict = storage.all()
        if len(args) == 0:
            print("** class name doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
