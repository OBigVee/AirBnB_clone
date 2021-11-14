#!/usr/bin/python3
""" the programm is the entry point of the command interpreter """


import cmd, sys


class HBNBCommand(cmd.Cmd):
    intro = """\
	  Documented commands (type help <topic>):\n \
          ========================================\n \
          EOF  help  quit \n"""

    prompt = "(hbnb)"

    def __init__(self, completekey="tab", stdin=None, stdout=None):
        super().__init__(completekey, stdin, stdout)

    def do_quit(self, line):
        """leave the current program"""
        # Cmd.emptyline() == True
        return True

    def do_greet(self, line):
        """display interactive intro"""
        print(intro)

    def do_EOF(self, line):
        """quit CLI"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
