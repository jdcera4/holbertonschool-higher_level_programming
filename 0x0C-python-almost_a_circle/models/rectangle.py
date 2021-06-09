#!/usr/bin/python3
"""class rectangule """


from models.base import Base


class Rectangle(Base):
    """Reactangule"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ property widht"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter widdth"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

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
        self.__height = value

    @property
    def x(self):
        """Returns x as a private attribute"""

        return self.__x

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
        self.__x = value

    @property
    def y(self):
        """Returns y as a private attribute"""

        return self.__y

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
        self.__y = value

    def area(self):
        """return area """
        return self.__width * self.__height

    def display(self):
        """Prints a representation of the rectangle with '#'"""

        for space in range(self.__y):
            print("")

        for row in range(self.__height):
            for move in range(self.__x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """str"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.__height))

    def update(self, *args, **kwargs):
        """update"""
        attrubutes = ["id", "width", "height", "x", "y"]
        for elem in range(len(args)):
            for attr in range(len(attrubutes)):
                if attr == elem:
                    setattr(self, attrubutes[attr], args[elem])

        if not args or len(args) == 0:
            for key, val in kwargs.items():
                for attr in range(len(attrubutes)):
                    if key == attrubutes[attr]:
                        setattr(self, attrubutes[attr], val)
