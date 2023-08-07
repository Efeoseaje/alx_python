""" A Rectangle class"""


BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A class Rectangle that inherits from BaseGeometry class """

    def __init__(self, width, height):
        """ Instantiation of the Rectangle class
        Args:
            width(int): width of the rectangle.
            height(int): height of the rectangle.
        raises:
            TypeError: if width or height is not an integer
            ValueError: if width or height is less or equal to 0.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
