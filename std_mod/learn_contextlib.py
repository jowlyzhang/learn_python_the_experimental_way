#!/usr/bin/python
"""This module experiments with the 'with ... as ...' syntax and
APIs in the contextlib module, including contextlib.closing()
contextlib.nested() which becomes a legacy after python2.7 when
nesting comes with the 'with' syntax, contextlib.contextmanager.
contextlib.closing() is used to support legacy handler classes that
has a close() method but not a __exit__ method so that they can also
properly cleans up in the context manager usage.
"""
import contextlib

# To support context manager, define a class with a __enter__
# and __exit__ methods.
class MyContext(object):

    def __init__(self):
        print 'in __init__'
        super(MyContext, self).__init__()

    # object returned by __enter__ is referred to by the variable
    # after 'as'
    def __enter__(self):
        print 'in __enter__'
        return self

    def do_something(self, a):
        print a

    # the type, value and traceback of an exception that is
    # raised by the code block within a with statement is passed
    # to the __exit__ function. If the code block handles its own
    # error, it won't be passed to __exit__ function.
    # __exit__ returning False would cause the error to be propogated.
    # __exit__ returning True would cause the error just to stop there.
    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'in __exit__'
        print exc_type
        print exc_val
        print exc_tb
        return True
        #return False

with MyContext() as mc:
    mc.do_something('didididi')
    raise AttributeError('an error in the with block')

# Another way to support context manager is by defining a generator.
# Compared to the above form of obeying the context manager APIs.
# object yielded would be referred to by the variable after 'as'.
# put what ever procedures that's in the __init__ function before
# the yield statement. Put whatever procedure that's in the __exit__
# function in the finally block. And raise again in the except block
# if the error is to be propogated.
@contextlib.contextmanager
def my_context(a):
    print 'entering'
    try:
        yield MyContext()
    # Compared to the above form,
    # there is only some specific type of errors that could be
    # explicitely caught.
    except AttributeError as e:
        #raise
        print str(e)
    finally:
        print 'exiting'

with my_context('something') as f:
    raise AttributeError('some error raised')

# After python2.7, the with statement has the nesting capability so
# contextlib.nested is legacy.
with my_context('a') as a, my_context('b') as b, my_context('c') as c:
    a.do_something('a_blabla')
    b.do_something('b_blabla')
    c.do_something('c_blabla')
