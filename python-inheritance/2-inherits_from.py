"""Checks if object is a subclass of a class"""


def inherits_from(obj, a_class):
    """ Returns True if the object is a subclass of the class """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
