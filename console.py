#!/usr/bin/python3

""" Console 0.1 """

import ast
import shlex
import cmd
import sys
from models import storage
from models.city import City
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Class that defines a small command interpreter """
    prompt = "(hbnb) "

    my_dict = {'Amenity': Amenity, 'BaseModel': BaseModel, 'City': City,
               'Place': Place, 'Review': Review, 'State': State, 'User': User}

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
        elif arg[0] in self.my_dict:
            object = getattr(sys.modules[__name__], arg[0])
            inst = object()
            print(inst.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """prints the string representaiton of an string"""
        objdict = storage.all()
        arg = args.split(" ")
        if arg[0] is None or arg[0] == "":
            print("** class name missing **")
        if arg[0] in self.my_dict:
            if len(arg) == 1:
                print("** instance id  missing **")
                return
            arguments1_2 = f"{arg[0]}.{arg[1]}"
            if arguments1_2 not in objdict:
                print("** no instance found **")
                return
            print(storage.all()[arguments1_2])
        else:
            print("** class doesn't exist **")
            return

    def do_destroy(self, args):
        """ deletes an instance based on the class name and id """
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
        """ prints allstring representation of all instances
        based or not on the class name """
        args.split(" ")
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name doesn't exist **")

    def do_update(self, arg):
        """update an instance based on the class name and id"""
        arg = shlex.split(arg)
        if len(arg) < 1:
            print("** class name missing **")
            return
        if arg[0] not in self.my_dict:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        obj = storage.get_object(arg[1])
        if obj:
            if len(arg) < 3:
                print("** attribute name missing **")
            elif len(arg) < 4:
                print("** value missing **")
            else:
                """check invalid data type"""
                try:
                    setattr(obj, arg[2], ast.literal_eval(arg[3].strip()))
                except (ValueError, SyntaxError):
                    setattr(obj, arg[2], arg[3])
                obj.save()
        else:
            print("** no instance found **")
            

if __name__ == '__main__':
    HBNBCommand().cmdloop()
