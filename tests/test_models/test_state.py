#!/usr/bin/python3
"""Unit tests for the State class"""

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Unit tests for the State class"""

    def test_instance(self):
        """Test if an instance of State is correctly created"""
        instance = State()
        self.assertIsInstance(instance, State)

    def test_state_name(self):
        """Test the default state name"""
        instance = State()
        self.assertEqual("", instance.name)

    def test_id(self):
        """Test if the id attribute is of type string"""
        instance = State()
        self.assertEqual(str, type(instance.id))


if __name__ == "__main__":
    unittest.main()
