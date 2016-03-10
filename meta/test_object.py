#!/usr/bin/python
import pdb

class MetaA(type):
    def __call__(meta_cls, name, bases, dct):
        cls = type.__call__(type, name, bases, dct)
        return  type(meta_cls, name, bases, dct)

    def __new__(meta_cls, name, bases, dct):
        cls = type.__new__(meta_cls, name, bases, dct)
        return cls

    def __init__(cls, *args, **kwds):
        print 'self: {}'.format(cls)


class A(object):
    __metaclass__ = MetaA
    #def __call__(*args, **kwds):
    #    print 'in the call'

    def __new__(cls, *args, **kwds):
        self = object.__new__()
        self.__init__(*args, **kwds)

    def __init__(self, *args, **kwds):
        print 'self: {}'.format(self)

a = A()
a()

class type():
    def __call__(meta_cls, name, bases, dct):
        meta_cls.__new__(name, bases, dct)

    def __new__(meta_cls, names, bases, dct):
        cls_obj = get_some_memory_space()
        self.__add_namespace(cls_obj, dct)
        self.__link_to_ancestors(cls_obj, bases)
        self.__init__(cls_obj)

    # placeholder for customized initialization.
    def __init__(cls, *args, **kwd):
        pass

class MetaA(type):

    # Don't do this, don't try to override the ___call__ method
    # Just call super()
    #def __call__(meta_cls, name, bases, dct):
    #    pass

    def __new__():
        pass
