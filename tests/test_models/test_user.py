#!/usr/bin/python3
"""Unit tests for the User class"""

from opcode import hasconst
import unittest
from models.user import User
import datetime


class UserCase(unittest.TestCase):
    """Unit tests for the User class"""

    user = User()

    def test_class_exists(self):
        """Test if the User class correctly exists"""
        self.assertEqual(str(type(self.user)), "<class 'models.user.User'>")

    def test_user_inheritance(self):
        """Test if User class is a subclass of BaseModel"""
        self.assertIsInstance(self.user, User)

    def testHasAttributes(self):
        """Verify the existence of expected attributes in the User instance"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))

    def test_types(self):
        """Test if the attributes of the User instance have the correct data types"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)
        self.assertIsInstance(self.user.id, str)
        self.assertIsInstance(self.user.created_at, datetime.datetime)
        self.assertIsInstance(self.user.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
