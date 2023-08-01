#!/usr/bin/env python3
"""The entry stage of the program through a cli tool
"""

import cmd, sys
from models.base_model import BaseModel
from models.amenity import Amenity

class HBNBCommand(cmd.Cmd):
    #intro = "Welcome to the hbnb shell. Type help or ? to list commands.\n"
    
    prompt = "(hbnb)"

    available_classes = ["BaseModel", "User", "Amenity","Place","Review","State","City"]

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
    
    def do_create(self, line):
        """ Creates a new instance of BaseModel,
            saves it (to Json file) and prints the 
            id
        """
        args = line.split()
        if len(line) == 0:
            print("** class name missing **")
            return
        cls_name = line.split()[0]
        if cls_name not in self.available_classes:
            print("** class doesn't exist **")
            return
            #else:
        # base = BaseModel(cls_name)
        # base.save()
        # print(base.id)
        new_instance = eval(f"{cls_name}()")
        new_instance.save()
        print(new_instance.id)

    def do_show(self):
        print("{}".format(BaseModel.__class__.__name__,))

    def do_destroy(self):
        pass

    def do_all(self):
        pass

    def do_update(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
