#!/usr/bin/python
"""This module is an experiment comparing the difference of decorators with
parameters and decorators without parameters in the form of defining it as
a class, we will try to do the same thing in the form of defining it as a
function.

1. The syntax difference, with the `()` added following @SomeDecorator, that's
where the difference began.
    @DecwithoutParameter
    def somefunc()
At initinization:
    DecwithoutParameter(somefunc) which is esscentially
    DecwithoutParameter.__init__(somefunc) and if it's a class method, the pair
    (key: 'somefunc', value: <Class DecwithoutParameter object>) would be added
    to the `__dict__` attribute of that class.
During function calls:
    Calling this class method by syntax my_obj.somefunc(*args, **kwds) would do:
    exec(my_obj.__class__.__dict__['somefunc'].__get__(my_obj, my_obj.__class__), *args, **kwds)

with the magic we just learnt from implementation of staticmethod and classmethod, we know
that the above should work fine.

    @DecWithParameter(pam1=None, pam2=None)
    de somefunc()
At initialization:
    DecWithParameter(pam1=None, pam2=None) which is essentially
    DecWithParameter.__init__(pam1=None, pam2=None) would be called. Besides, it also
    calls DecWithParameter.__call__(somefunc), which returns a wrapped function. As
    it's also a class method, the pair (key: 'somefunc', value: <function wrapped_func>)
    would be added to its `__dict__`. But this `wrapped_func`function is a function that
    is defined within the scope of class DecWithParameter. Which essentially means the
    variable name `wrapped_func` points to a function handler that both its lifespan
    and scope lives within a class DecWithParameter object.

During function calls:
    my_obj.somefunc(*args, **kwds) would invoke wrapped_func(my_obj, *args, **kwds). Remember
    that `class function` also has a __get__protocol defined incase its a class attribute and
    accessed from there.

Comparing the above, we know that the difference lies in the protocol which is invoked by
different syntax, causing differnt lines of code to be executed at the time of initialization
and function calls. But we can make them both work fine as class method decorators with
intuitive calling syntax.
With a little bit of changed code, we can simply make both decorators work for standalone
functions too. And may also add something to make DecWithoutParameter to have the same magic
as what `functools.wraps` provides.
"""
from functools import wraps
import pdb

class DecWithParameter(object):
    def __init__(self, pam1=None, pam2=None):
        self.pam1 = pam1
        self.pam2 = pam2

    def __call__(self, func):
        self.func = func

        @wraps(func)
        def wrapped_func(*args, **kwds):
            print 'pam1: {}, pam2: {}'.format(self.pam1, self.pam2)
            return self.func(*args, **kwds)
        return wrapped_func


class DecWithoutParameter(object):
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
        self.instance = None
        self.cls = None

    def __get__(self, instance, cls):
        self.instance = instance
        self.cls = cls
        return self

    def __call__(self, *args, **kwds):
        if self.instance is None:
            return self.func(*args, **kwds)
        else:
            return self.func(self.instance, *args, **kwds)

    def __str__(self):
        if self.instance is None:
            return '<function {}>'.format(self.name)
        else:
            return '<bound method {} of {}>'.format(self.name, self.cls)


class Myclass(object):

    @DecWithoutParameter
    def func1(self, *args, **kwds):
        print 'self:{}, args:{}, kwds:{}'.format(self, args, kwds)


    @DecWithParameter(pam1=None, pam2=None)
    def func2(self, *args, **kwds):
        print 'self:{}, args:{}, kwds:{}'.format(self, args, kwds)


@DecWithoutParameter
def no_pam_func(*args, **kwds):
    print 'args:{}, kwds:{}'.format(args, kwds)


@DecWithParameter(pam1=None, pam2=None)
def pam_func(*args, **kwds):
    print 'args:{}, kwds:{}'.format(args, kwds)


if __name__ == '__main__':
    pdb.set_trace()
    my_obj = Myclass()
    print my_obj.func1
    my_obj.func1(1, 2, 3, timeout=8)
    print my_obj.func2
    my_obj.func2(4, 5, 6, timeout=7)
    print pam_func
    pam_func(1, 2, 3, timeout=7)
    print no_pam_func
    no_pam_func(4, 5, 6, timeout=8)
