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
            TypeError: if width, height, x, y is not an int.
            ValueError: if width, height is <= 0.
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
    
    @property
    def height(self):
        """ Retrieve the height """
        return self.__height
    
    @property
    def x(self):
        """ Retrieve the x-cordinate """
        return self.__x
    
    @property
    def y(self):
        """ Retrieve the y-cordinate """
        return self.__y
    

    @width.setter
    def width(self, value):
        """ Setting the right value for width of the rectangle"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @height.setter
    def height(self, value):
        """ Setting the right value for height of the rectangle """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @x.setter
    def x(self, value):
        """ Setting the right value for x-cordinate """
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")

    @y.setter
    def y(self, value):
        """ Setting the right value for y-cordinate """
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")