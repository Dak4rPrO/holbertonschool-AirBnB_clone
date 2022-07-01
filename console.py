#!/usr/bin/python3
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import cmd

"""command interpreter"""
"""from models import storage"""


class HBNBCommand(cmd.Cmd):
    """class of prompt"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ exit the program"""
        return True

    def emptyline(self):
        """dont do anything if theres an empty line"""
        pass
    
    def do_create(self, args):
        arg = parse(args)
        if len(arg) == 0:
            print("** class name missing **")

    def do_show(self, args):
        """prints the string representaiton of an string"""
        arg = parse(args)
        objdict = storage.all()
        if len(arg) == 0:
            print("** class doesn't exist **")
        elif arg[0] not in HBNBcommand.__class__:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id  mising **")
        elif "{}.{}".format(arg[0], arg[1]) not in objdict:
            print("** no instance found **")

    def do_destroy(self, args):
        """deletes an instance based on the class name and id"""
        arg = parse(args)
        objdict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBcommand.__class__:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in objdict:
            print("** no instance found **")

    def all(self, args):
        """prints allstring representation of all instances
        based or not on the class name"""
        arg = parse(args)
        objdict = storage.all()
        if len(arg) == 0:
            print("** class name doesn't exist **") 

if __name__ == '__main__':
    HBNBCommand().cmdloop()