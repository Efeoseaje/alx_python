""" Defines a Square"""


class Square:
    """ a class that defines a Square """
    
    def __init__(self, size=0):
        """ Initializes the square class
        Args: 
            size: represents the size of the square
        """

        self.__size = size

    @property
    def size(self):
        """ retrieves the size """
        return self.__size
    
    @size.setter
    def size(self, value):
        """ Sets the size 
        Args:
            value: represents the size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0. 
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Computes and returns the current square area """
        return (self.__size ** 2)
    
    def my_print(self):
        """ Prints in stdout the square with the character # """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)