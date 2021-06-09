#!/usr/bin/python3
"""Unittest for Square class"""
import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Runs tests for square.py"""

    @classmethod
    def setUpClass(cls):
        """Sets up the testing environment"""

        Base = _Base__nb_objects = 0
        cls.s1 = Square(5)
        cls.s2 = Square(7)
        cls.s3 = Square(2, 2)
        cls.s4 = Square(3, 1, 2)

    def test_10_00_create(self):
        """Checks to see if the creation of a square was successful"""

        self.assertTrue(self.s1)
        self.assertTrue(self.s2)
        self.assertTrue(self.s3)
        self.assertTrue(self.s4)