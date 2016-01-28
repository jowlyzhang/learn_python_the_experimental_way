#!/usr/bin/python
"""The objects in python that are callable.
"""
class Myfunc(object):
    def __init__(self, *args):
        self.args = args
        self.__name__ = self.__class__.__name__

    def __get__(self, instance, cls):
        self.__self__ = instance
        self.__func__ = self
        self.cls = cls
        return self

    def __call__(self, *args):
        if len(args) != len(self.args):
            raise ValueError('requires {} arguments'.format(len(self.args)))
        print args

# class is callable those defined with the `class` keyword. calling them
# should generally instatiate a new instance of that class. However you
# can customize that.
class WildClass(object):
    # Assume this serves the same purpose as defining a class
    # method using the line of code below
    # def wild_func(a, b, c):
    # the characters, 'a', 'b', 'c' are place holders to define
    # how many arguments this function takes.
    wild_method = Myfunc('a', 'b', 'c')

    def __new__(cls, *args, **kwds):
        print 'I am a verbose instantiator'
        new_instance = object.__new__(cls)
        cls.__init__(new_instance, *args, **kwds)
        return new_instance

    def __init__(self, name):
        self.name = name

    def cls_method(self):
        print 'I am a class method'

    def __call__(self, *args, **kwds):
        print 'I make class instances callable'

def reg_func(*args, **kwds):
    print 'I am a regular customized function'

wild_func = Myfunc('a', 'b', 'c')

def gene_func():
    i = 0
    while True:
        yield i
        i + 1

if __name__ == '__main__':
    # class is callable
    a = WildClass('balabala')
    # class instance is callable
    # if __call__ is implemented
    a()
    # instance method is callable
    # an instance method combines a class, a class instance, arguments
    # and keywords to a callable object (a customer defined function, or
    # some other callable things)
    # It has all the regular function attributes plus the special
    # `__self__` attribute which is the class instance binded to it.
    a.cls_method()
    print a.cls_method.__self__
    print a.cls_method.__name__
    print a.cls_method.__doc__
    print a.cls_method.__module__
    print a.cls_method.__func__

    a.wild_method('babala', 'dododo', 'dididid')
    print a.wild_method.__self__
    print a.wild_method.__name__
    print a.wild_method.__doc__
    print a.wild_method.__module__
    print a.wild_method.__func__
    # customized function is callable
    reg_func()
    wild_func('babala', 'dododo', 'dididdi')
    # builtin function is callable
    print id(a)
    # builtin instance method is callable
    print [1, 2, 3].insert(0, 9)
    # generator function is callable
    ge = gene_func()
    print next(ge)
