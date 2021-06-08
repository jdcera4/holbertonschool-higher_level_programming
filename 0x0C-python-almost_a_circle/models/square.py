#!/usr/bin/python3
"""square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """clas square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes class Square"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overwrites the __str__ magic method"""

        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))