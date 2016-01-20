#!/usr/bin/python
"""This module is an experiment comparing the difference of decorators with
parameters and decorators without parameters in the form of defining it as
a function.

Check test_dec.py for the previous experiment. This one is looks even more
elegant.
"""
from functools import wraps
import pdb

def DecWithParameter(pam1=None, pam2=None):

    def dec_hd(func):

        @wraps(func)
        def wrapped_func(*args, **kwds):
            print 'pam1: {}, pam2: {}'.format(pam1, pam2)
            return func(*args, **kwds)
        return wrapped_func

    return dec_hd



def DecWithoutParameter(func):
    @wraps(func)
    def wrapped_func(*args, **kwds):
        return func(*args, **kwds)
    return wrapped_func


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
    my_obj = Myclass()
    print my_obj.func1
    my_obj.func1(1, 2, 3, timeout=8)
    print my_obj.func2
    my_obj.func2(4, 5, 6, timeout=7)
    print pam_func
    pam_func(1, 2, 3, timeout=7)
    print no_pam_func
    no_pam_func(4, 5, 6, timeout=8)
