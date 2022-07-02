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
    my_dict= {'Amenity' : Amenity, 'BaseModel' : BaseModel, 'City' : City,
              'Place' : Place, 'Review' : Review, 'State' : State, 'User' : User}

    def do_quit(self, args):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, args):
        """ exit the program"""
        return True

    def emptyline(self):
        """ aca deje solo el self, porque si pones el args, da Traceback. cuando leas esto, borra el comentario xd """
        """dont do anything if theres an empty line"""
        pass

    def do_create(self, args):
        """ def create """
        args.split(" ")
        with open(file.json, 'r') as f:
            json.dump(self., f)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.my_dict:
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