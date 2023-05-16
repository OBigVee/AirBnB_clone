#!/usr/bin/env python3
""" The entry stage of the progam through a cli tool
"""

import cmd, sys

class HBNBCommand(cmd.Cmd):
    #intro = "Welcome to the hbnb shell. Type help or ? to list commands.\n"
    
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """end of file """
        return True

    def do_emptyline(self):
        pass

    def do_help(self, line):
        """ list the action that be performed"""
        super().do_help(line)

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
