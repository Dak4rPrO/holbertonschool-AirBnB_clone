#!/usr/bin/python3
"""
command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
	"""class of prompt"""

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
