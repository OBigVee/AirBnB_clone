#!/usr/bin/env python3
"""The entry stage of the program through a cli tool
"""

import cmd
import re
from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage


class HBNBCommand(cmd.Cmd):
    # intro = "Welcome to the hbnb shell. Type help or ? to list commands.\n"

    prompt = "(hbnb)"

    available_classes = [
        "BaseModel",
        "User",
        "Amenity",
        "Place",
        "Review",
        "State",
        "City",
    ]

    valid_classes = ['BaseModel', 'User', 'State', 'City',
                     'Amenity', 'Place', 'Review']

    def do_EOF(self, line):
        """end of file"""
        return True

    def do_emptyline(self):
        pass

    def do_help(self, line):
        """list the action that be performed"""
        super().do_help(line)

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to Json file) and prints the
        id
        """
        args = line.split()
        if len(line) == 0:
            print("** class name missing **")
            return
        
        cls_name = args[0]
        if cls_name not in self.available_classes:
            print("** class doesn't exist **")
        
        else:
            # base = BaseModel(cls_name)
            # base.save()
            # print(base.id)
            new_instance = eval(f"{cls_name}()")
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """show <class> <instance id>
        do_show prints the string representation
        of the instance with matching `instance id`.

        The valid classes are:
        <classes>: [
            'BaseModel', 'User',
            'State', 'City',
            'Amenity', 'Place',
            'Review'
        ]
        """

        argv = line.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif len(argv) >= 1 and argv[0] not in self.available_classes:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        else:
            # print the string representation of the object
            storage.reload()
            objs = storage.all()
            key = "{}.{}".format(argv[0], argv[1])
            try:
                obj = objs[key]
                print(obj)
            except KeyError:
                print("** no instance found **")

        # args = line.split()

        # if len(args) == 0:
        #     print("** class name missing **")
        #     return
        # cls_name = args[0]

        # if cls_name not in self.available_classes:
        #     print("** class doesn't exist **")

        # elif len(args) < 2:
        #     print("** instance id missing **")
        #     return
        
        # attr_id = args[1]
        # storage.reload()
        # all_objs = storage.all()
        # obj_keys = f"{cls_name}.{attr_id}"
        
        # if obj_keys in all_objs:
        #     print(all_objs[obj_keys])
        # else:
        #     print("** no instance found **")

            # try:
            #     print(all_objs[obj_keys])
            # except KeyError:
            #     print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and `id`
        save the change into the JSON file.
        Usage: destroy  <class> <instance id>
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in self.available_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        attr_id = args[1]
        #storage.reload()
        all_objs = storage.all()
        obj_keys = f"{cls_name}.{attr_id}"

        try:
            del all_objs[obj_keys]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """do_all: prints all string representation of all 
        instances based or not on the class name.
        Usage: all <class name> or all
        """
        # args = line.split()
        # storage.reload()
        # all_objs = storage.all()

        # if len(args) == 0:
        #     print([str(obj) for obj in all_objs.values()])
        # else:
        #     cls_name = args[0]
        #     if cls_name not in self.available_classes:
        #         print("** class doesn't exist **")
        #         return
            
        #     filtered_objs = [str(obj) for key, obj in all_objs.items()]
        #     print(filtered_objs)
        argv = line.split()
        if len(argv) >= 1 and argv[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(argv) >= 1 and argv[0] in self.valid_classes:
            # Print a list containing only specified class objects
            return_list = []
            storage.reload()
            objs = storage.all()
            for key, obj in objs.items():
                if key == ("" + argv[0] + "." + obj.__dict__["id"]):
                    return_list.append(obj.__str__())
            print(return_list)
        else:
            # Print a list containing all class objects in storage
            return_list = []
            storage.reload()
            objs = storage.all()
            for key, obj in objs.items():
                return_list.append(obj.__str__())
            print(return_list)

    def do_update(self, line):
        """Updates an instance based on the class name and `id` by adding
        or updating attribute (save the changes into the JSON file). 
        Ex: update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        Usage: update <class name> <id> <attribute name> `<attribute value>`
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in self.available_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        
        attr_id = args[1]
        storage.reload()
        all_objs = storage.all()
        obj_key = f"{cls_name}.{attr_id}"

        try:
            objs = all_objs[obj_key]
            print(objs)
        except KeyError:
            print("** no instance found **")

        if len(args) < 3:
            print("** attribute name missing **")
            return
        
        attr_name = args[2]

        # storage.reload()
        # all_objs = storage.all()
        # obj_key = f"{cls_name}.{attr_name}"

        # try:
        #     objs = all_objs[obj_key]
        #     print(objs)
        # except KeyError:
        #     print("** attribute name missing **")
        
        if len(args) < 4:
            print("** value missing **")
        else:
            try:
                storage.reload()
                all_objs = storage.all()
                obj_key = f"{cls_name}.{attr_id}"
                obj = all_objs[obj_key]

                try:
                    # get the type of the attribute
                    Type = type(obj.__dict__[attr_name]) 
                    # cast the attribute type on attribute value
                    obj.__dict__[attr_name] = Type(args[3].strip("\""))
                except KeyError:
                    obj.__dict__[attr_name] = args[3].strip("\"")
                obj.save()

            except KeyError:
                print("** no instance found **")

    def parseline(self, line):
        """
        Parse every line before returning it back to the console.
        Looking out for match such as the following for extra
        processing:
        + <class name>.all()
        + <class name>.count()
        + <class name>.show(<id>)
        + <class name>.destroy(<id>)
        + <class name>.update(<id>, <attribute name>, <attribute value>)
        + <class name>.update(<id>, <dictionary representation>)
        """
        lone_commands = ['all', 'quit', 'EOF', 'help']
        argv = line.split()
        matched = re.search(r"\w+\.\w+\(", line)

        if len(argv) == 0:  # Handles empty line
            return line, line, line

        if (len(argv) != 1 or argv[0] in lone_commands) and not matched:
            # Do for commands that required arguments or
            # commands that works alone.
            return argv[0], " ".join(argv[1:]), line

        # Additional parsing for aliases listed in string doc.
        # example: class.command(args)
        if matched:
            _class, argv = line.split(".", 1)  # ['class', 'command(args)']
            cmd, argv = argv.split("(", 1)  # ['command', 'args)']
            argv = argv.replace(")", '')  # 'args)' -> 'args'

            matched = re.search(r"{.+}", argv)  # checking for dict definition
            if matched:  # if dictionary exists in arguements
                objs = storage.all()
                import json
                obj_id, argv_dict = argv.split(", ", 1)  # ['<id>', '<dict>']
                argv_dict = argv_dict.replace("'", "\"")
                obj_id = obj_id.replace("\"", "")
                argv_dict = json.loads(argv_dict)
                key = "{}.{}".format(_class, obj_id)
                try:
                    obj = objs[key]
                    obj.__dict__.update(argv_dict)
                    obj.save()
                except KeyError:
                    print("** no instance found **")

                line = ""
                return line, line, line

            if cmd == "count":  # handles <class>.count()
                objs = storage.all()
                count = 0
                for key, obj in objs.items():
                    if obj.__class__.__name__ == _class:
                        count = count + 1
                print(count)
                line = ''
                return line, line, line
            return cmd, _class + " " + " ".join(argv.split(", ")), line

        return argv[0], " ".join(argv[1:]), line

if __name__ == "__main__":
    HBNBCommand().cmdloop()
