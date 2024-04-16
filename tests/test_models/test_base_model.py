#!/usr/bin/python3
"""Unit tests for the BaseModel class"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test suite for the BaseModel class"""

    def test_save(self):
        """Test that the save method updates the updated_at attribute to the current datetime"""
        base = BaseModel()
        old_time = base.updated_at
        base.save()
        self.assertNotEqual(old_time, base.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method to ensure it:
            - Returns a dictionary
            - Contains all keys/values from the instance's __dict__ attribute
            - Includes the '__class__' key with the class name of the instance
        """
        base = BaseModel()

        # Verify it returns a dictionary
        base_dict = base.to_dict()
        self.assertIsInstance(base_dict, dict)

        # Check if the dictionary contains '__class__' key with the class name
        self.assertTrue("__class__" in base_dict)
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertEqual(str(base.id), base_dict["id"])
        self.assertIsInstance(base_dict["created_at"], str)
        self.assertIsInstance(base_dict["updated_at"], str)

    def test_str(self):
        """Test that the string representation of an instance is formatted correctly"""
        base = BaseModel()
        right_format = f"[{type(base).__name__}] ({base.id}) {base.__dict__}"
        self.assertEqual(str(base), right_format)


if __name__ == "__main__":
    unittest.main()
