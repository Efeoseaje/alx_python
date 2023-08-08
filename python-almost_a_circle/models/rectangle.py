""" A Rectangle class that inherits from Base class """

from models.base import Base


class Rectangle(Base):
    """  A class that defines a rectangle and inherits from base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantiation of the Rectangle class
        Args:
            width(int): the width of the rectangle
            height(int): the height of the rectangle
            x(int): the x cordinate of the rectangle
            y(int): the y cordinate of the rectangle
            id(int): the identity of the rectangle.

        Raises:
            TypeError: if width, height is not an int.
            ValueError: if width, height is <= 0.
            TypeError: if x, y is not an int.
            ValueError: if x, y is < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Retrieve the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setting the right value for width of the rectangle"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ Retrieve the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setting the right value for height of the rectangle """
        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ Retrieve the x-cordinate """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setting the right value for x-cordinate """
        if (type(value) is not int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ Retrieve the y-cordinate """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setting the right value for y-cordinate """
        if (type(value) is not int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ Returns the area value of the Rectangle instance """
        return (self.__width * self.__height)

    def display(self):
        """ Prints the rectangle to stdout with the character '#' """
        for i in range(self.__height):
            print('#' * self.__width)

    def __str__(self) -> str:
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
            {self.width}/{self.height}"
