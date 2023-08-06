"""A BaseGeometry class"""


class MetaGeometry(type):
    """ A class used to define the behaviour of class BaseGeometry"""

    def __dir__(MetaGeometry):
        """ A special method used to customize the behaviour of dir()
        Args:
            MetaGeometry: The metaclass to customize it's attributes
        
        Return:
            Returns all attributes of the metaclass except '__init_subclass__' attribute
        """
        return [attributes for attributes in super().__dir__() if attributes != '__init_subclass__']


class BaseGeometry(metaclass=MetaGeometry):
    """The base geometry class that inherits from a metaclass"""
    
    def __dir__(BaseGeometry):
        """ A special method used to customize the behaviour of dir()
        Args:
            BaseGeometry: The class to customize it's attributes
        
        Return:
            Returns all attributes of the class except '__init_subclass__' attribute
        """
        return [attributes for attributes in super().__dir__() if attributes != '__init_subclass__']
    
    def area(self):
        """ Area not implemented yet
        raises: an exception with the message 'area() is not implemented'
        """

        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """ Validates a given value as an integer
        Args:
            name(str): name of the parameter being validated
            value(int): parameter to be validated
        raise:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0.
        """
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')

        

