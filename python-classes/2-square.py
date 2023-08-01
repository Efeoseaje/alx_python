""" Defines a Square"""


class Square:
    """ a class that defines a Square """
    
    def __init__(self, size=0):
        """ Initializes the square class
        Args: 
            size: represents the size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size

    
    def area(self):
        """ Computes and returns the current square area """
        return (self.__size ** 2)
