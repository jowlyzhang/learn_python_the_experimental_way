#!/usr/bin/python
"""Module explaination: this is an experiment trying to build a
user specific staticmethod and classmethod decorator.

There are few basic things to understand here:
    1. @staticmethod and @classmethod are just decorators with the syntax
    sugar that should follow the protocol for decorators without parameters.
    2. Attribute of the class that has one or more of '__get__', '__set__',
    '__del__'functions defined are descriptors and would follow the protocol
    for descriptors.
    3. the operator `()` added to an object, say `regular_func` would make
    python treat that object as a function handler or call its `__call__`
    method if there is one.
    Note: with this said. __get__ can both return self.__call__ and self
    This is validated by experiment.

With the above rule #1:
    @Mystaticmethod
    def func1(*args, **kwds):
        pass

    would add (key:'func1', value:<class Mystaticmethod object>) pair to the `__dict__`
    of class `Myclass`. And the <class Mystaticmethod object> is initiated with
    function handler func1 passed as the only argument.

With the above rule #2:
    if a = Myclass()
    when doing a.func1(*args, **kwds) will revoke descriptor protocol of __get__ and translates to
    a.__class__.__dict__['func1'].__get__(a, a.__class__)
    which will pass both the object and the class to the __get__ function of the descriptor
    that was initiated.

With the above rule #3:
    continue what happened following rule #2, the returned object of __get__ function is
    `self.__call__` which is a function handler or `self` which has an attribute `__call__`,
    `*args, **kwds` will be passed to `__call__` and you can implement whatever rules
    that needs to be implementd to make it look like it's following the concept of a
    staticmethod or classmethod or a regular method.

The function binding magic of class methods and the static method
are solved with the combined power of descriptor, decorator and python magic functions.
The most important take away class is everything in python is an object, including a
function, that's why it shouldn't bother to model regular class methods as a descriptor
here.
"""
class Myclassmethod(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        self.instance = instance
        self.cls = cls
        return self

    def __call__(self, *args, **kwds):
        return self.func(self.cls, *args, **kwds)


class Combomethod(object):
    """A descriptor and decorator that makes a method called
    as a class method and instance method. I haven't figured out the whole
    bound method magic, it could also turned out to be a completely builtin
    in methanism. So now, a previous bound method of a class/class instance
    would end up being an instance of Combomethod. However, I can maually
    tailor the print out message to hide this fact.
    """
    def __init__(self, func):
        self.func = func
        self.__name__ = self.func.__name__
        self.__doc__ = self.func.__doc__
        self.__dict__.update(self.func.__dict__)

    def __str__(self):
        if self.instance is not None:
            return '<bound method {} of <class {}>>'.format(self.__name__, self.cls)
        else:
            return 'unbound method {}.{}'.format(self.cls, self.__name__)

    def __format__(self):
        return self.__str__()

    def __get__(self, instance, cls):
        self.instance = instance
        self.cls = cls
        return self

    def __call__(self, *args, **kwds):
        if self.instance is not None:
            return self.func(self.instance, *args, **kwds)
        else:
            return self.func(self.cls, *args, **kwds)


class Mystaticmethod(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        self.instance = instance
        self.cls = cls
        return self

    def __call__(self, *args, **kwds):
        return self.func(*args, **kwds)


class Regularmethod(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance ,cls):
        self.instance = instance
        self.cls = cls
        return self

    def __call__(self, *args, **kwds):
        if self.instance is None:
            raise Exception('regular method must be called with a class object')
        return self.func(self.instance, *args, **kwds)


class Myclass(object):

    @Myclassmethod
    def class_method(cls, *args, **kwds):
        print 'in a class method'
        print 'class: {}'.format(cls)
        print 'args: {}'.format(args)
        print 'kwds: {}'.format(kwds)

    @Mystaticmethod
    def static_method(*args, **kwds):
        print 'in a staticmethod'
        print 'args: {}'.format(args)
        print 'kwds: {}'.format(kwds)

    @Regularmethod
    def regular_func(self, *args, **kwds):
        print 'in a regular'
        print 'self: {}'.format(self)
        print 'args: {}'.format(args)
        print 'kwds: {}'.format(kwds)


if __name__ == '__main__':
    Myclass().static_method(3, 4)
    Myclass.static_method(3, timeout=2)
    Myclass().class_method(3, 4)
    Myclass.class_method(3, timeout=2)
    Myclass().regular_func(3, timeout=1)
    Myclass.regular_func(3, 4)
