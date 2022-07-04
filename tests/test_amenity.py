#!/usr/bin/python3
"""
    module
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import pep8


class AmenityTest(unittest.TestCase):
    """test"""

    def test_sub_class(self):
        """is an sublcass"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_style(self):
        """tests pep8"""
        style = pep8.StyleGuide(quit=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_instance(self):
        """is an instance"""
        am = Amenity()
        self.assertEqual(am.name, "")
        self.assertTrue(isinstance(am, BaseModel))


if __name__ == '__main__':
    unittest.main()
