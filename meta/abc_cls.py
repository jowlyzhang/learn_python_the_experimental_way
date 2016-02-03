#!/usr/bin/python
from abc import ABCMeta, abstractmethod, abstractproperty
import pdb

pdb.set_trace()
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        instance = type.__new__(cls, name, bases, dct)
        cls.__init__(instance)
        return instance

class 
