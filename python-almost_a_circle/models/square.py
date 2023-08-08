""" A class that defines a square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """  A class that defines a square and inherits from the rectangle class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Instantiation of the Square class
        Args:
            size(int): the width and height of the square
            x(int): the x cordinate of the square
            y(int): the y cordinate of the square
            id(int): the identity of the square.

        Raises:
            TypeError: if size is not an int.
            ValueError: if size is <= 0.
            TypeError: if x, y is not an int.
            ValueError: if x, y is < 0.
        """
        # self.size = size
        # self.x = x
        # self.y = y
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Retrieve the size """
        return self.__width

    @size.setter
    def size(self, value):
        """ Setting the right value for width of the square"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value
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
        """ Returns the area value of the square instance """
        return super().area()

    def display(self):
        """ Prints the square to stdout with the character '#' """
        # return super().display()
        for y in range(self.y):
            print()
        for i in range(self.width):
            for x in range(self.x):
                print(" ", end="")
            print('#' * self.width)

    def __str__(self):
        """ Overides the string representation of the square """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """ Assigns arguments to each attribute
        Args:
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
        """
        if args and len(args) != 0:
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                elif index == 1:
                    self.size = value
                elif index == 2:
                    self.x = value
                elif index == 3:
                    self.y = value

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'size':
                    self.size = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v