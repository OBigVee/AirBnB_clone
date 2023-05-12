#!/usr/bin/python3
"""test for BaseModel class and it corresponding functions"""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class Test_BaseModel(unittest.TestCase):

    def test_instance_id_is_unique(self):
        """ test for id making sure ids are unique """
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_save(self):
        """ test for save method """
        from time import sleep
        base = BaseModel()
        sleep(2)
        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)
    
    def test_str_rep(self):
        """test for __str__ method """
        base = BaseModel()
        str_output = "[{}] ({}) {}".format(base.__class__.__name__,
                base.id, base.__dict__)
        self.maxDiff = None
        self.assertEqual(base.__str__(), str_output)

        
    def test_to_dict(self):
        """ test for to_dict method"""
        base = BaseModel()
        model_json = base.to_dict()
        base2 = BaseModel(**model_json)
        self.assertFalse(base is base2)

    def test_instance_datatime_variable(self):
        """ method test for """
        base = BaseModel()
        model_json = base.to_dict()
        base2 = BaseModel(**model_json)
        self.assertEqual(type(base.created_at), datetime)
        self.assertEqual(type(base.updated_at), datetime)
