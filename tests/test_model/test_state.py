#!/usr/bin/python3
""" unittest for our base model class """

import models
from models.state import State
import os
from datetime import datetime
import unittest
from time import sleep


class StateInstantiationTest(unittest.TestCase):
    """ Test cases for instantiation """

    def test_empty_args(self):
        self.assertEqual(State, type(State()))

    def test_new_obj_is_in_storage_obj(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_public(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_two_obj_have_diff_id(self):
        bm1 = State()
        bm2 = State()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_obj_have_diff_created_at(self):
        bm1 = State()
        sleep(0.06)
        bm2 = State()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_obj_have_diff_updated_at(self):
        bm1 = State()
        sleep(0.06)
        bm2 = State()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = State()
        bm.id = "123"
        bm.created_at = bm.updated_at = dt_repr
        bm_str = bm.__str__()
        self.assertIn("[State] (123)", bm_str)
        self.assertIn("'created_at': '{}'".format(dt_repr), bm_str)
        self.assertIn("'updated_at': '{}'".format(dt_repr), bm_str)
        self.assertIn("'id': '123'", bm_str)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_str = dt.isoformat()
        bm = State(id="123", created_at=dt_str, updated_at=dt_str)
        self.assertEqual(bm.id, "123")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_args_is_unused(self):
        bm = State(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_none_kwarg_args(self):
        with self.assertRaises(TypeError):
            bm = State(id=None, created_at=None, updated_at=None)

    def test_instance_with_arg_and_kwarg(self):
        dt = datetime.today()
        dt_str = dt.isoformat()
        bm = State("12", id="123", created_at=dt_str, updated_at=dt_str)
        self.assertEqual(bm.id, "123")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)
        self.assertNotIn("12", bm.__dict__.values())


# class TESTSAVE(unittest.TestCase):

#     @classmethod
#     def setUp(self):
#         try:
#             os.rename("file.json","tmp")
#         except IOError:
#             pass

#     @classmethod
#     def tearDown(self):
#         try:
#             os.remove("file.json")
#         except IOError:
#             pass

#         try:
#             os.rename("tmp", "file.json")
#         except IOError:
#             pass

#     def test_one_save(self):
#         bm = State()
#         sleep(0.06)
#         first_updated_at = bm.updated_at
#         print(models.storage.save())
#         bm.save()
#         self.assertLess(first_updated_at, bm.updated_at)
#     def test_two_save(self):
#         bm = State()
#         sleep(0.05)
#         first_update_at = bm.updated_at
#         bm.save()
#         self.assertLess(first_update_at, bm.updated_at)
#         second_updated_at = bm.updated_at
#         sleep(0.06)
#         bm.save()
#         self.assertLess(second_updated_at, bm.updated_at)

#     def test_save_with_arg(self):
#         bm = State(None)
#         with self.assertRaises(TypeError):
#             bm.save(None)

#     def test_save_updates_file(self):
#         bm = State()
#         bm.save()
#         bmid = "State."+bm.id
#         with open("file.json") as f:
#             self.assertIn(bmid, f.read())

class TEST_To_Dict(unittest.TestCase):
    def test_type(self):
        bm = State()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_dict_contains_correct_keys(self):
        bm = State()
        self.assertIn("id", bm.to_dict().keys())
        self.assertIn("created_at", bm.to_dict().keys())
        self.assertIn("updated_at", bm.to_dict().keys())
        self.assertIn("__class__", bm.to_dict().keys())

    def test_created_and_updated_are_str(self):
        bm = State()
        bmdict = bm.to_dict()
        self.assertEqual(str, type(bmdict["created_at"]))
        self.assertEqual(str, type(bmdict["updated_at"]))

    def test_passing_arg(self):
        bm = State()
        with self.assertRaises(TypeError):
            bmdict = bm.to_dict(None)

    def test_additional_attributes_added(self):
        bm = State()
        bm.name = "mbuke prince"
        self.assertIn("name", bm.to_dict().keys())

    def test_dict_attr_is_diff_to_to_dit(self):
        bm = State()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = State()
        bm.id = "123"
        bm.updated_at = bm.created_at = dt

        bmdict = {
            "id": "123",
            "created_at": dt.isoformat(),
            "updated_at": dt.isoformat(),
            "__class__": 'State'
        }
        self.assertDictEqual(bm.to_dict(), bmdict)

if __name__ == "__main__":
    unittest.main()
