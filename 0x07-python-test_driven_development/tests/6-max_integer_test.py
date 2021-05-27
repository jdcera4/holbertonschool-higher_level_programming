#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_ax_error(self):
        self.assertEqual(max_integer([1, 2, 5]), 5)
        self.assertEqual(max_integer([-1, 2, -5]), 2)
        self.assertEqual(max_integer([-1, -2, -5]), -1)
        self.assertEqual(max_integer([1, 2, 5, 6, 7, 10]), 10)

    def test_string(self):
        self.assertRaises(TypeError, max_integer(['a', 'b', 'c']))


