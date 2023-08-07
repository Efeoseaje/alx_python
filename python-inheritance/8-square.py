""" A Square class"""


Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """ A class Square that inherits from Rectangle class """

    def __init__(self, size):
        """ Instantiation of the Square class
        Args:
            size(int): size of the Square.

        raises:
            TypeError: if size is not an integer
            ValueError: if size is less or equal to 0.
        """
        self.__size = size  # stores the sides in a private attribute
        self.integer_validator("size", size)
        """instantiation of the square with two attributes(width and height which are the same)"""
        super().__init__(size, size)  

    def area(self):
        """ Computes the area of the Square
        Returns:
            The area of the Square
        """
        return super().area() # utilizes the area method from the rectangle
