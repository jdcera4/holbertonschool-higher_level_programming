#!/usr/bin/python3
"""Unittest foralmost a circle / Rectangle
"""
import unittest
import io
import sys
import os
import models.rectangle
from models.rectangle import Rectangle
from models.base import Base
class Test_Rectangle_Requeriments(unittest.TestCase):
    """Class to test the Rectangle class requeriments"""
    # Testing pep8 and shebang
    def test_pep8(os_system):
        """PEP8 validation"""
        os_system.assertEqual(os.system("pep8 ./models/rectangle.py"), 0)
    def test_shebang(self):
        """First line contains #!/usr/bin/python3"""
        with open('./models/rectangle.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')
    # Documentation for Module, class and methods exist
    def test_docmodule(self):
        """Module is documented"""
        temp = models.rectangle.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
    def test_docclass(self):
        """Class is documented"""
        temp = Rectangle.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
    def test_doc_getters(self):
        """Functions getter are documented"""
        # Getters
        temp = Rectangle.__init__.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
        temp = Rectangle.width.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
        temp = Rectangle.height.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
        temp = Rectangle.x.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
        temp = Rectangle.y.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
    def test_doc_methods(self):
        """Functions are documented"""
        # Area
        temp = Rectangle.area.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
        # Str
        temp = Rectangle.__str__.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
        # Update
        temp = Rectangle.update.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
# Test for task 2. First Rectangle
class Test_Rectangle(unittest.TestCase):
    """Class to test the Rectangle class funcionalities"""
    def setUp(self):
        """setup nb_objectes to 0 after each test"""
        Base._Base__nb_objects = 0
    # Task 2
    def test_rectangle_constructor(self):
        """Correct Output"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
