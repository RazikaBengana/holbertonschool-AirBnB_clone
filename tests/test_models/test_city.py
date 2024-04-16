#!/usr/bin/python3
"""Unit tests for the City class"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test suite for the City class"""

    def test_instance(self):
        """Test if the object is an instance of the City class"""
        hohio = City()
        self.assertIsInstance(hohio, City)

    def test_city_name(self):
        """Test the name attribute of the City class"""
        hohio = City()
        self.assertEqual("", hohio.name)

    def test_id(self):
        """Test the ID attribute of the City class"""
        hohio = City()
        self.assertEqual(str, type(hohio.id))

    def test_state_id(self):
        """Test the state ID attribute of the City class"""
        hohio = City()
        self.assertEqual("", hohio.state_id)


if __name__ == "__main__":
    unittest.main()
