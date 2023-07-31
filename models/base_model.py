#!/usr/bin/env python3
""" BaseModel class"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs.pop("__class__", None)
            for k, v in kwargs.items():
                setattr(self, k, v)
            if "created_at" in kwargs:
                value = kwargs["created_at"]
                created_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, "created_at", created_at)

            if "updated_at" in kwargs:
                value = kwargs["updated_at"]
                updated_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, "updated_at", updated_at)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of instance
        """
        d_dict = {"__class__": self.__class__.__name__}
        d_dict.update(self.__dict__)
        d_dict["created_at"] = self.created_at.isoformat()
        d_dict["updated_at"] = self.updated_at.isoformat()
        return d_dict

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
