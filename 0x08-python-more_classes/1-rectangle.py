#!/usr/bin/python3
"""rentangle class"""


class Rectangle:
    """define Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the data"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Initializes the data"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """setter of width, for create the conditionals"""
        if type(value) is int:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__value = value
        else:
            raise TypeError("width must be an integer")
    
    @property
    def width(self):
        """Initializes the data"""
        return self.__height
    
    @width.setter
    def width(self, value):
        """setter of width, for create the conditionals"""
        if type(value) is int:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__value = value
        else:
            raise TypeError("width must be an integer")
