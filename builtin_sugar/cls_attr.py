#!/usr/bin/python
"""This module is used to experiment how python stores class attributes and
object instance attributes.
>>> dir(cls) would give a list of attributes of the class itself and recursively its
base classes.
some of the always see attributes that most likely inherites from the `object` class are:
    1. __delattr__, __getattribute__, __setattr__, __hash__, __dict__,related to attribute operations.
    2. __new__, __init__ related to new instance initialization.
    3. __doc__, __str__, __repr_, __format__ related to documentation of the class
    4. __module__, __class__ related to identity
    6. __sizeof__, __reduce__, __reduce_ex_, __subclasshook__, __weakref__
    7. its own and its ancestor class's class variables and methods.
    split as inherited from ancestors and belong to itself
    1. __dict__, __module__, __weakref__, __doc__ are the attributes that are generated
    from the code definition itself.
    2. __delattr__, __getattribute__, __setattr__, __hash__, __new__, __init__,
    __str__, __repr__, __format__, __class__, __sizeof__, __reduce__, __reduce_ex__,
    __subclasshook__ are inherited from `object`and you can of course override it.

>>> dir(instance) would give a list of attributes that that pretty much the same as
dir(instance.__class__) plus its own instance variables.


>>> vars(cls) would give a dict of attributes of a class that looks simply like the result
from parsing the code of that class definition directly. This is exactly the same as
cls.__dict__
    1.__module__, __doc__
    2. methods and class variables that are defined within that class, not its ancestor.

>>> vars(instance) gives a dictionary of instance variables

To sum up, vars(something) and something.__dict__ return the same dictionary, only
attributes of that `something` itself, not its ancestors. For class, it gives class
methods, class variables and some basic class attributes. For class instance, it only
gives the instance variables.

dir(something) gives a list of attibutes of that `something` and its ancestors.
For class, it gives class methods, class variables, and its inherited such things, which
include some very useful attributes inherited from the `object` class as listed above.
For class instances, aside from the attributes for class, it also has gives the instance
variables.

>>> class BaseClass(object):
        pass

>>> class InheClass(BaseClass):
        pass

>>> myinstance = InheClass()
>>> print myinstance.a

would invoke such an order of looking for `a`
    1. Is `a` in vars(myinstance) namely myinstance.__dict__
    2. Is `a` in vars(InheClass) namely InheClass.__dict__
    3. Is `a` in vars(BaseClass) namely BaseClass.__dict__
with the same logic when you do:
>>> myinstance.__dict__
    1. Is `__dict__` in myinstance.__dict__ ---> No
    2. Is `__dict__` in InheClass.__dict__ ---> No
    3. Is `__dict__` in BaseClass.__dict__ ---> Yes and it's a getset_descriptor
"""
class Dog(object):
    breed='pudo'

    def __init__(self, name):
        self.name = name

    def bark(self):
        print 'wang wang wang....'


class BigDog(Dog):
    weight=22


class SmallDog(Dog):
    weight=10

if __name__ == '__main__':
    dog = Dog('regulardog')
    bg = BigDog('oversizeddog')
    sg = SmallDog('poordog')
    print 'Dog vars: {}'.format(vars(Dog))
    print 'Dog __dict__["__dict__"]: {}'.format(Dog.__dict__['__dict__'])
    print 'BigDog vars: {}'.format(vars(BigDog))
    print 'BigDog __dict__: {}'.format(BigDog.__dict__)
    print 'SmallDog vars: {}'.format(vars(SmallDog))
    print 'SmallDog __dict__: {}'.format(SmallDog.__dict__)
    #print 'Dog dir: {}'.format(dir(Dog))
    #print 'BigDog dir: {}'.format(dir(BigDog))
    #print 'SmallDog dir: {}'.format(dir(SmallDog))
    print 'dog vars: {}'.format(vars(dog))
    print 'dog __dict__: {}'.format(dog.__dict__)
    print 'bg vars: {}'.format(vars(bg))
    print 'bg __dict__: {}'.format(bg.__dict__)
    print 'sg vars: {}'.format(vars(sg))
    print 'sg __dict__: {}'.format(sg.__dict__)
    #print 'dog dir: {}'.format(dir(dog))
    #print 'sg dir: {}'.format(dir(sg))
    #print 'bg dir: {}'.format(dir(bg))
