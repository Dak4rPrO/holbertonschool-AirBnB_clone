#!/usr/bin/python3


import cmd

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
        super().do_help(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
