#!/usr/bin/python3
"""Module to Write a class Square that defines a square
"""


class Square():
    """
    This is a class Square that defines a square

    This class can be used as a starting point for creating new classes
    or as a placeholder for future development.

    Example usage:
        emp = Square()

    Attributes:
        size: the size of the square sides defaults to 0

    Methods:
        __init__: constructor method to initialize the square
        size: the size of the square sides defaults to 0
        position: tuple of default 0,0
    Args:
        position: tuple of default 0,0
        size: the size of the square sides defaults to 0

    """

    def __init__(self, size=0, position=(0, 0)):
        """The  __init__ method for the class Square.

        The init method takes in a protected parameter size defaulted to 0

        Args:
            size: the size of the square sides defaults to 0
            position: tuple of default 0,0
        Raises:
            TypeError: If size or position is not an integer or tuple
            ValueError: If size is negative.
        """
        if not isinstance(position, tuple) and len(position) != 2:
            if not all(isinstance(x, int) and x > 0 for x in position):
                raise TypeError("Position must be a tuple of 2 positive integers")

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        """This defines the area of the square

        The area of the square

        Returns:
            int: the area of the square
        """
        area = self.__size
        return area * area

    def my_print(self):
        """This defines the area of the square

        The area of the square

        Prints the square using the stored size and position attributes.
        If size is 0, prints an empty line.
        """
        side = self.__size
        space = self.__position

        if side == 0:
            print()
        else:
            for i in range(side):
                if space[1] > 0:
                    print("_", end="")
                else:
                    for i in range(space[0]):
                        print("_", end="")
                for j in range(side):
                    print("#", end='')
                print()

    @property
    def size(self):
        """Getter method for the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute
        Args:
            value (int): The new value for the size attribute.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for the position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for the position attribute
        Args:
            value (tuple): The new value for the position attribute.
        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if isinstance(position, tuple) and len(position) == 2:
            if all(isinstance(x, int) and x > 0 for x in position):
                return position
        else:
            raise TypeError("Position must be a tuple of 2 positive integers")
        self.__position = value
