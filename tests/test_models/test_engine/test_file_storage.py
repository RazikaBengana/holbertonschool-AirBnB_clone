#!/usr/bin/python3
"""Unit tests for the FileStorage class"""

import json
import os.path
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unit tests for the FileStorage class"""

    def test_instantiates(self):
        """Test that FileStorage is instantiated correctly"""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_file_path(self):
        """Test that the file path type is a string after deserialization"""
        file_path_str = FileStorage._FileStorage__file_path
        self.assertEqual(str, type(file_path_str))

    def test_objects(self):
        """Test that the objects attribute is a dictionary after deserialization"""
        object_dict = FileStorage._FileStorage__objects
        self.assertEqual(dict, type(object_dict))

    def test_all(self):
        """Test the all() method of FileStorage"""
        dict_return = {}
        FileStorage.all(None)
        self.assertTrue(os.path.isfile('file.json'))  # Check if 'file.json' exists


if __name__ == "__main__":
    unittest.main()
