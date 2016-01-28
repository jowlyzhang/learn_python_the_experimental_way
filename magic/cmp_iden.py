#!/usr/bin/python
"""This module is for experimenting with Python's way of identity and comparison of
customer defined class objects.

identity of an object is unique upon its creation and unchangeable, retrieved with id(),
you can think of it as the object's address in memory. The `is` operator is
basically comparing two objects' identities. The behavior of the compareing operators
including `==`, `!=`, `<=`, `>=`, `<`, `>` for a customer defined class are defined
by the below magic methods. __eq__, __ne__, __le__, __ge__, __lt__, __gt__ and a
once-and-for-all magic method __cmp__, that not only defines behavior of the above operators
but also of the builtin function cmp().

type of an object is also unchangeable, retrieved with type(), it determines operations
this object supports and possible values it could have.
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

    # __hash__ magic method is called by the builtin hash() function to
    # create a hash value when a class instance is used as a dictionary key
    # and the hash value can be used for quick key comparison. Note that
    # the hash value is not used directly as the key. Below, it's verified.
    def __hash__(self):
        return ord(self.name[0])

if __name__ == '__main__':
    a = MyClass('lili')
    b = MyClass('dili')
    c = MyClass('lily')
    print a is b
    print a is c
    print b is c
    print id(a), id(b), id(c)
    print a == c
    print a < b
    test_dict = {}
    test_dict[a] = 'lili'
    test_dict[c] = 'lily'
    # Looks like the hash value is not used directly as the dictionary
    # Key. How dictionary compute and stores key can be another topic
    # we'll look into next time.
    for i in range(0, 10):
        print test_dict[a], test_dict[c]

