#!/usr/bin/python3
"""defines a class called Square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data"""
        self.__size = size
        self.position = position

    @property
    def size(self):
        """Initializes the data"""
        return self.__size

    @property
    def position(self):
        """Initializes the data"""
        return self.__position

    @size.setter
    def size(self, size):
        """setter size"""
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, value):
        """stter position"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(isinstance(value, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print #"""
        if self.__size == 0:
            print("")
        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print()

        for row in range(self.__size):
            if self.__position[0] > 0:

                for row in range(self.__position[0]):
                    print(" ", end="")
                for columns in range(self.__size):
                    print("#", end="")
                print("")
