#!/usr/bin/python3
""" the programm is the entry point of the command interpreter """

from models.base_model import BaseModel
from models import storage
from shlex import split
import cmd


class HBNBCommand(cmd.Cmd):
    """ Defines the HBnB command interpleter
    Attributes:
        prompt (str): command prompt
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """ Responds for empty line entry"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """quit CLI"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
