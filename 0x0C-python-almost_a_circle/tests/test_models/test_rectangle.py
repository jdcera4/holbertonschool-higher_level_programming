#!/usr/bin/python3
"""test rectangle"""
import unittest
import os
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