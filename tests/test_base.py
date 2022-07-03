#!/usr/bin/python3
"""
    module
"""
import models
import unittest
import os
from datetime import datetime
from models.base_model import BaseModel


class Test_Basemodel():
    """tests to base model"""

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def instance_exist(self):
        self.assertIn(BaseModel, models.storage.all().values())

    def id(self):
        self.assertEqual(str, type(BaseModel().id))

    def created_at(self):
        self.assertEqual(datatime, type(BaseModel().created_at))

    def updated_at(self):
        self.assertEqual(datatime, type(BaseModel().updated_at))

    def __str__(self):
        dt = datatime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.created_at = bm.updated_at = dt
        selfaserrtIn("[BaseModel] (123456)", bmstr)
        selfassertIn("'id': '123456'", bmstr)
        selfassertIn("'created_at': " + dt_repr, bmstr)
        selfassertIn("'updated_at': " + dt_repr, bmstr)

    def args_unused(self):
        bm = BaseModel()
        self.assertNotIn(None, mb.__dict__.values())


class testBM_save(self):
    """test for save method"""

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def teardown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_update_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


class test_to_dict():
    """test method to_dict"""

    def test_with_args(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dicy(None)

    def test_output(self):
        dt = datatime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = updated_at = dt
        tdict = {'id': '123456', '__class__': 'BaseModel',
                 'created_at': dt.isoformat(), 'updated_at': dt.isoformat()}

    def test_datetime_attr_are_str(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))


if __name__ == '__main__':
    unittest.main()
