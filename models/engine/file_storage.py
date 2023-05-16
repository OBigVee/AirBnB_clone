#!usr/bin/env python3
""" storage class serializes instances to a JSON file
    and deserializes JSON file to instances
"""

import json

class FileStorage:

    """Private class attributes """
    __file_path = "file.json"
    __objects = {}

    """Public instance methods"""

    def all(self):
        """ returns dictionary objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with k
            <obj class name>.id
        """
        from models.base_model import BaseModel
        if obj and isinstance(obj, BaseModel):
            k = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[k] = obj
    
    def save(self):
        """ save method serializes __objects to
            the JSON file path: __file_path
        """
        obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as file_obj:
            json.dump(obj_dict, file_obj)

    def reload(self):
        """deserializes the json file to __objects
            (only if the JSON file (__file_path)
            exits; otherwise, do nothing. if the file
            doesn't exit, no exception should be raised)
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as obj_file:
                from models.base_model import BaseModel
                obj_f = json.loads(obj_file.read())
                FileStorage.__objects = {}
                for k,v in obj_f.items():
                    _class =v["__class__"]
                    _obj = eval("{}({})".format(_class, "**v"))
                    self.new(_obj)
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass