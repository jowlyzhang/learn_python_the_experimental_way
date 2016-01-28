#!/usr/bin/python
"""To peak into attributes of class and instances more closely.
This would explain why dog_a.name would give 'lina', and dog_b.name would give
'losh'.
Class and objects supports access to attributes both through the attribute operator,
(Implemented via the class or its metaclass's __getattribute__ method). and the __dict__
attribute protocol which also supports vars(). To be more specific:
    1. Accessing instance attributes as in a.b invokes python to call:
    type(a).__getattrbute__(a, 'b')

    2. Assigning values to instance attributes as in a.b = 'something' invokes python
    to call:
    type(a).__setattr__(a, 'b', 'something'):

With that implemented explicitely by overriding the metaclass's __getattribute__
and __setattr__ functions, the following logic simply follows.

assgning dog_a.name = 'lina' would invoke:
    -> Dog.__setattr__(dog_a, 'name', 'lina')
    which invokes:
    -> Dog.__dict__['__dict__'].__get__(dog_a, Dog)['name'] = 'lina'

accessing dog_a.name would invoke:
    -> Dog.__getattribute__(dog_a, 'name')
    which invokes:
    -> Dog.__dict__['__dict__'].__get__(dog_a, Dob)['name']

That's how a class stores variables for different instances.
There could be more complecation when it comes to how class
store their attributes. But it wouldn't be so hard with the
idea that class is also objects in python.

Just explicitely pointing out the magic methods of dict type.
Nothing special.
"""
class MyDict(dict):
    def __setitem__(self, key, value):
        return dict.__setitem__(self, key, value)

    def __getitem__(self, key):
        return dict.__getitem__(self, key)

    def __delitem__(self, key):
        return dict.__delitem__(self, key)

    def __contains__(self, key):
        return dict.__contains__(self, key)


class MyGetSetDescriptor(object):
    def __init__(self, name):
        self.name = name
        self.all_insts_vars = {}

    def __get__(self, instance, cls):
        if instance not in self.all_insts_vars:
            self.all_insts_vars[instance] = MyDict()
            instance.__dict__  = self.all_insts_vars[instance]
        return self.all_insts_vars[instance]


class Dog(object):
    __dict__ = MyGetSetDescriptor(name='__dict__')
    color = 'red'

    def __init__(self, name):
        self.name = name

    def __getattr__(self, name):
        if name == 'special':
            return 'that is the special attribute'
        else:
            raise AttributeError('No such attribute')

    def __getattribute__(self, attr_name):
        print '\nVerbose getter\n'
        try:
            return Dog.__dict__['__dict__'].__get__(self, Dog)[attr_name]
        except KeyError:
            pass

        try:
            return Dog.__dict__[attr_name].__get__(self, Dog)
        except (KeyError, AttributeError):
            pass

        try:
            return Dog.__dict__[attr_name]
        except KeyError:
            pass

        try:
            return self.__getattr__(attr_name)
        except AttributeError:
            raise

    def __setattr__(self, attr_name, value):
        print '\nVerbose setter\n'
        Dog.__dict__['__dict__'].__get__(self, Dog)[attr_name] = value

    def __delattr__(self, attr_name):
        print '\nVerbose Deletter\n'
        del Dog.__dict__['__dict__'].__get__(self, Dog)[attr_name]



if __name__ == '__main__':
    dog_a = Dog('lina')
    dog_b = Dog('losh')
    print dog_a.name, dog_b.name
    dog_a.weight = 3
    dog_b.weight = 5
    print dog_a.weight, dog_b.weight
    print dog_a.__dict__, dog_b.__dict__
    print type(dog_a.__dict__)
    print type(Dog.__dict__['__dict__'])
    print dog_a.color, dog_b.color
    del dog_a.weight
    print dog_a.special
