#!/usr/bin/python3
"""
    module
"""
import unittest
import pep8
from models.base_models import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """test an user"""

    def test_instance(self):
        """if instance"""
        u = User()
        self.assertEqual(u.email, "")
        self.assertEqual(u.passqord, "")
        self.assertEqual(u.first_name, "")
        self.assertEuqal(u.last_name, "")
        self.assertTrue(isinstance(u, BaseModel))

    def test_pep8(self):
        """test check"""



if __name__ == '__main__':
    unittest.main()
