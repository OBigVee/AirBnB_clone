#!/usr/bin/python3
""" Defines FileStorage engine """

import json
from models.base_model import BaseModel


class FileStorage:
    """ Performs serialization and deserialization functionarity.

    Attributes:
      __file_path(str): path to the json file to store objects
      __objects(dict): dictionary containing all objects
    """
    __file_path = "file.json"
    __objects = dict({})

    def all(self):
        """ returns all objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets __objects with new obj """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """ serializes the __objects to json"""
        odict = FileStorage.__objects
        ob_dict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(ob_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
