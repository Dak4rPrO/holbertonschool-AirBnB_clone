#!/usr/bin/python3
"""
command interpreter
"""
"""from models import storage"""
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import cmd

class HBNBCommand(cmd.Cmd):
	"""class of prompt"""
	prompt = '(hbnb)'

	def do_quit(self, arg):
		"""quit the shell"""
		return 1

	def do_EOF(self, arg):
		"""quit the shell"""
		print()
		return 1

	def emptyline(self):
		"""don't do anything if there's an empty line"""
		return 0

if __name__ == '__main__':
    HBNBCommand().cmdloop()