#!/usr/bin/python
"""
To quote the python3 official documentation. Custom class types are created by class definition.
    1. A class has a namespace implemented by a dictionary object, __dict__
    2. Class attribute reference are translated to lookups in this dictionary
    C.x translates to C.__dict__['x'].
    3. When the attribute name is not found here, the attribute search continues
    in the base classes (there is an algorithm involved for the order of base classes
    to search that works fine even in case of `diamond` ring inheritance structures).
    4. When a class attribute reference would yield a class method object, like when you
    do MyClass.stat_func(), it transforms into an instance method object with __self__ attribute
    defined as MyClass.
    5. Class attribute assignments updates the class's dictionay, not the dictionary of its base class.

Builtin class attributes include:
    1. __name__, the class name
    2. __module__, module name in which class is defined
    3. __dict__, class namespaces.
    4. __bases__ tuple (singleton) containing base classes.
    5. __doc__, class doc string


Class instances:
    1. A class instance has a namespace implemented as a dictionary, __dict__
    2. Instance variable access mo.x translates to mo.__dict__['x'] first.
    3. When the attribute name is not found here and the instance class has an
    attribute of that name, it continues search in the class attributes, and if
    the attribute is a user defined function, it transformed into an instance
    method variable whose __self__ attribute is the instance.
    4. If no class attribute with this name is found and the class has a __getattr__
    implemented. It would go there to satisfy the lookup request
    5. Instance attributes update would update only the __dict__ of the instance, not
    the class, if the class has __setattr__, __delattr__ defined, it would go there first.

"""

class MyClass(object):

    @staticmethod
    def stat_func(a, b):
        print 'I am just a regular method'

    def reg_func(self):
        print 'I am even more regular'


if __name__ == '__main__':
    mo = MyClass()
    MyClass.stat_func()
    mo.reg_func()
