#!/usr/bin/python3
"""Unit tests for the Review class"""

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Unit tests for the Review class"""

    def test_review_text(self):
        """Test that the initial text attribute is empty"""
        review_instance = Review()
        self.assertEqual("", review_instance.text)


if __name__ == '__main__':
    unittest.main()
