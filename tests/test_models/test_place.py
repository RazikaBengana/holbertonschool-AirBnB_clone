#!/usr/bin/python3
"""Unit tests for the Place class"""

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestState(unittest.TestCase):
    """Unit tests for the Place class"""

    def test_place_isinstance(self):
        """Test if an object is an instance of the Place class"""
        somewhere = Place()
        self.assertIsInstance(somewhere, Place)

    def test_place_name(self):
        """Test that the default name attribute is an empty string"""
        a = Place()
        self.assertEqual("", a.name)


if __name__ == "__main__":
    unittest.main()
