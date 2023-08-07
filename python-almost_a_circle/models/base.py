""" A base class """


class Base:
    """ A base class from which all other classes inherit 
    Attributes:
        nb_objects: Number of instantiated objects of the class
    """
    __nb_objects = 0


    def __init__(self, id=None):
        """ Instantiation of the base class
        Args:
            id(int): the id of the new base.
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

