#!/usr/bin/python3
"""class rectangule """
from models.base import Base


class Rectangle(Base):
    """Reactangule"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self._width = value

    @property
    def height(self):
        """Returns height as a private attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """Defines the height
        Args:
            value: integer that represents the height
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self._height = value

    @property
    def x(self):
        """Returns x as a private attribute"""

        return self._x

    @x.setter
    def x(self, value):
        """Defines the x
        Args:
            value: integer that represents the x
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self._x = value

    @property
    def y(self):
        """Returns y as a private attribute"""

        return self._y

    @y.setter
    def y(self, value):
        """Defines the y
        Args:
            value: integer that represents the y
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self._y = value

    def area(self):
        return self._width * self._height

    def display(self):
        """Prints a representation of the rectangle with '#'"""

        for space in range(self._y):
            print("")

        for row in range(self._height):
            for move in range(self._x):
                print(" ", end="")
            for col in range(self._width):
                print("#", end="")
            print("")

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.__height))
