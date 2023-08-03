"""Checks if object is a subclass of a class"""


def is_kind_of_class(obj, a_class):
    """ Returns True if the object is an inherited instance of the class """
    if issubclass(obj, a_class):
        return True
    else:
        return False
