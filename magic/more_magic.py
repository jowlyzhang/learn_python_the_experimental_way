#!/usr/bin/python
"""A few of the magic methods inherited from the `object` class
to support behavior of customer defined classes are exprimented in
other modules. Listed below:
    In the cmp_iden module:__eq__, __ne__, __le__, __ge__, __lt__
    __gt__, __cmp__, __hash__.
    In the py_callable module: __new__, __init__, __call__, __get__,
    and __set__.
    In cls_attr2 module: __getattribute__, __setattr__, __delattr__

This module is for trying out some other magic methods that are listed
below and can be generally split into four groups.
    1. docstring formatting: __str__, __format__, __repr__
    it's looks very straight forward when these different functions would be invoked.
    but why there are such difference is the good question to ask.
"""
class MyClass(object):

    def __str__(self):
        return '__str__ returns'

    def __repr__(self):
        return '__repr__ returns'

    def __format__(self, formatstr):
        return msg + '__format__ returns'


if __name__ == '__main__':
    mo = MyClass()
    print str(mo)
    print repr(mo)
    print '{}'.format(mo)
