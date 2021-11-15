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
    prompt = "(hbnb)"
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
        }

    def emptyline(self):
        """ Responds for empty line entry"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """quit CLI"""
        return True

    def do_create(self, arg):
        """
            usage: create <classname>
            creates a new object of class <classname>
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            bm = eval(arg)()
            print(bm.id)
            storage.save()

    def do_show(self, arg):
        """
            usage: show <id>
            show object with id <id>
        """
        obj = storage.all()
        line = arg.split()
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            if len(line) == 1:
                print("** instance id missing **")
            else:
                if "{}.{}".format(line[0], line[1]) not in obj.keys():
                    print("** no instance found **")
                else:
                    print(obj["{}.{}".format(line[0], line[1])])

    def do_destroy(self, arg):
        """
            usage: destroy <id>
            destroys an object with id <id>
        """
        obj = storage.all()
        line = arg.split()
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            if len(line) == 1:
                print("** instance id missing **")
            else:
                if "{}.{}".format(line[0], line[1]) not in obj.keys():
                    print("** no instance found **")
                else:
                    del obj["{}.{}".format(line[0], line[1])]
                    storage.save()

    def do_all(self, arg):
        """
            usage: all <classname?>
            lists all objects
        """
        if len(arg) > 0 and arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objs = []
            for obj in storage.all().values():
                if len(arg) > 0 and arg == obj.__class__.__name__:
                    objs.append(obj.__str__())
                elif len(arg) == 0:
                    objs.append(obj.__str__())
            print(objs)

    def do_update(self, arg):
        """
            usage: update <classname> <id> <attribute> <value>
            updates attribute of object of id with value
        """
        argl = arg.split()
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]

if __name__ == "__main__":
    HBNBCommand().cmdloop()
