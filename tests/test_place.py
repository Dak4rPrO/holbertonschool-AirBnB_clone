#!/usr/bin/python3
"""
    module
"""
import unittest
import pep8
from models.place import Place
from models.base_model import BaseModel


class test_place(unittest.TestCase):
    """test place"""

    def sub_class(self):
        """is a subclass"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attrs(self):
        """test attribut"""
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])

    """def check_functions(self):
        check
        self.assertIsNotNone(Place.__doc__)"""

    def test_instance(self):
        """test instances"""
        places = Place()
        self.assertEqual(places.city_id, "")
        self.assertEqual(places.user_id, "")
        self.assertEqual(places.name, "")
        self.assertEqual(places.number_rooms, 0)
        self.assertEqual(places.number_bathrooms, 0)
        self.assertEqual(places.description, "")
        self.assertEqual(places.price_by_night, 0)
        self.assertEqual(places.max_guest, 0)
        self.assertEqual(places.latitude, 0.0)
        self.assertEqual(places.longitude, 0.0)
        self.assertEqual(places.amenity_ids, [])
        self.assertTrue(isinstance(places, BaseModel))

if __name__ == '__main__':
    unittest.main()
