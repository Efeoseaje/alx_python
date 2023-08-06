"""An empty class"""


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
    """This is an empty class"""
    
    def __dir__(BaseGeometry):
        """ A special method used to customize the behaviour of dir()
        Args:
            BaseGeometry: The class to customize it's attributes
        
        Return:
            Returns all attributes of the class except '__init_subclass__' attribute
        """
        return [attributes for attributes in super().__dir__() if attributes != '__init_subclass__']
