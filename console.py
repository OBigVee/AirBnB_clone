#!/usr/bin/python3
""" the programm is the entry point of the command interpreter """



import cmd,sys

class HBNBCommand(cmd.Cmd):
    intro = """ \Documented commands (type help <topic>):\
                ========================================\
                EOF  help  quit\ """
    prompt = "(hbnb)"

    


