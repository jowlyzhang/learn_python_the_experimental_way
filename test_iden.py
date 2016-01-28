#!/usr/bin/python
"""This module is for experimenting with Python's way of identity of
objects.
>>> a = MyClass('lili')
    b = MyClass('dili')
    c = MyClass('lily')
    print id(a), id(b), id(c)

identity of an object is unique upon its creation and unchangeable, retrieved with id(),
you can think of it as the object's address in memory. The `is` operator is
basically comparing two objects' identities.

type of an object is also unchangeable, retrieved with type(), it determines operations
this object supports and possible values it could have
"""

class MyClass(object):
    def __init__(self, name):
        self.name = name

    def __eq__(self, another_instance):
        return self.name == another_instance.name

    def __ne__(self, another_instance):
        return self.name != another_instance.name

    def __le__(self, another_instance):
        return self.name[0] <= another_instance.name[0]

    def __ge__(self, another_instance):
        return self.name[0] >= another_instance.name[0]

    def __lt__(self, another_instance):
        #return self.name[0] < another_instance.name[0]
        return NotImplemented

    def __gt__(self, another_instance):
        return self.name[0] > another_instance.name[0]

    # Defineing this magic method served as the same purpose as
    # defining a whole bunch of the above comaprison methods. Just
    # make sure that a negative value is returned what should be
    # interpreted as less, a positive value is return for what should
    # be interpreted as greater.
    """def __cmp__(self, another_instance):
        if ord(self.name[0]) == ord(another_instance.name[0]):
            return 0
        elif ord(self.name[0]) < ord(another_instance.name[0]):
            return -1
        elif ord(self.name[0]) > ord(another_instance.name[0]):
            return 1"""


    def __hash__(self):
        return ord(self.name[0])


