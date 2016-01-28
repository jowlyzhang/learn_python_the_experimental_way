"""A few of the magic methods inherited from the `object` class
to support behavior of customer defined classes are exprimented in
other modules. Listed below:
    In the cmp_iden module:__eq__, __ne__, __le__, __ge__, __lt__
    __gt__, __cmp__, __hash__.
    In the py_callable module: __new__, __init__, __call__, __get__,
    and __set__.

This module is for trying out some other magic methods that are listed
below and can be generally split into three parts.
"""
class MyObject(object):
    def __delattr__(self):
        pass

    def __getattribute__(self):
        pass

    def __setattr__(self):
        pass
    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __format__(self):
        pass

    def __reduce__(self):
        pass

    def __reduce_ex__(self):
        pass

    def __sizeof__(self):
        pass

    def __weakref__(self):
        pass

    def __subclasshook__(self):
        pass


if __name__ == '__main__':
    print dir(MyObject)
