#!/usr/bin/python3
"""rentangle class"""


class Rectangle:
    """define Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the data"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Initializes the data"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height, for create the conditionals"""
        if type(value) is int:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """Calculation Area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculation perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Prints a string representation of a rectangle with #"""

        if self.__width == 0 or self.__height == 0:
            return ""
        cont = ""
        for row in range(self.__height):
            for columns in range(self.__width):
                cont = cont + str(self.print_symbol)
            if row == self.__height - 1:
                break
            else:
                cont = cont + "\n"
        return cont

    def __repr__(self):
        """Returns the name of the class with attributes"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method
        args:
        rect_1:
        rect_2:
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            return rect_1
