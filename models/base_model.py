#!/usr/bin/python3
""" BaseModel class"""

import uuid
from datetime import datetime

class BaseModel:
    
    def __init__(self, *args, **kwargs):
        # self.id = str(uuid.uuid4())
        # self.created_at = datetime.today()
        # self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for k,v in kwargs.items():
                if k == "__class__":
                    if k in ["created_at", "updated_at"]:
                        self.__dict__[k] = datetime.strptime(v, self.tformat)
                    else:
                        self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = dateime.now()

    def save(self):
        """updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = str(datetime.now())
        #self.updated_at = datetime.datetime
    
    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of instance
        """
        return self.__dict__

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
