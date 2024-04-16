#!/usr/bin/python3
"""Unit tests for the Amenity class"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unit tests for the Amenity class"""

    def test_class(self):
        """Test if the created object is an instance of Amenity"""
        testamenity = Amenity()
        self.assertEqual(testamenity.__class__.__name__, "Amenity")

    def test_attributes_Class(self):
        """Test the attributes of the Amenity class"""
        my_amenity = Amenity()
        my_amenity.name = "Hello-Holberton"
        self.assertEqual(my_amenity.name, 'Hello-Holberton')

    def test_subclass(self):
        """Test if Amenity is a subclass of BaseModel"""
        testamenity = Amenity()
        self.assertTrue(issubclass(testamenity.__class__, BaseModel))

    def test_Amenity_name(self):
        """Test the default name attribute of Amenity"""
        a = Amenity()
        self.assertEqual("", a.name)


if __name__ == "__main__":
    unittest.main()
