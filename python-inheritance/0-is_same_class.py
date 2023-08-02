"""Checks if object is an instance of a class"""


def is_same_class(obj, a_class):
    """ Returns True if the object is exactly an instance of the class """
    if isinstance(obj, a_class):
        return True
    else:
        return False
