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
        """test str"""
        mb = BaseModel()
        self.assertEqual(f"[{type(bm).__name__}] ({bm.id}) {bm.__dict__}", str(m))

    def args_unused(self):
        bm = BaseModel()
        self.assertNotIn(None, mb.__dict__.values())

    def test_save(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


    def test_with_args(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)

    def test_output(self):
        dt = datatime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = updated_at = dt
        tdict = {'id': '123456', '__class__': 'BaseModel',
                 'created_at': dt.isoformat(), 'updated_at': dt.isoformat()}

    def equal_or_not(self):
        """equals"""
        id_to_compare = BaseModel()
        id_compare = BaseModel()
        self.assertNotEqual(id_compare, id_to_compare)

    def test_datetime_attr_are_str(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def tests_to_dict(self):
        """test dict"""
        bm = BaseModel()
        self.assertEqual(bm.to_dict()["id"], bm.id)
        self.assertEqual(bm.to_dict()["created_at"], bm.created_at.isoformat())
        self.assertEqual(bm.to_dict()["updated_at"], bm.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
