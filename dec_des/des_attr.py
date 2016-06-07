"""There comes together a very interesting memory layout graph to explain this topic
a littler bit more 'pattr.jpg'. Also a list of all 'type', 'object' builtin methods
in attr_list.
Before we go ahead and learn about how descriptors work. Let's first experiment
how the python built-in instance, class attributes are stored.
"""
class A(object):pass
a = A()
type(A) # type of a class is 'type'
type(a) # type of class instance 'a' is 'A'
type(a.__dict__) # <type 'dict'>
type(A.__dict__) # <type 'dictproxy'>
type(type.__dict__) # <type 'dictproxy'>
type(A.__dict__['__dict__']) # # <type 'getset_descriptor'>
type(type.__dict__['__dict__']) # <type 'getset_descriptor'>
a.__dict__ == A.__dict__['__dict__'].__get__(a) # True
A.__dict__ == type.__dict__['__dict__'].__get__(A) # True
a.__dict__ == type.__dict__['__dict__'].__get__(A)['__dict__'].__get__(a) # True

# The above example shows the relationship between the '__dict__' attributes.
# It shows that class objects' attributes are stored in its class, class's attributes
# are stored in its metaclass.

a.__dict__ == A.__getattribute__(a, '__dict__') # True
A.__dict__ == type.__getattribute__(A, '__dict__') # True
a.__dict__ == type.__getattribute__(A, '__dict__')['__dict__'].__get__(a, '__dict__') # True

# The above example shows that __getattribute__ is a method to manipulate instance attributes,
# class attributes that stores in the '__dict__' of a class object or classes. Below example
# confirm this.

class A(object):
    def __getattribute__(self, name):
        print 'customer getattribute method'
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        print 'customer setattr method'
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        print 'customer delattr method'
        object.__delattr__(self, name)

a = A()
a.didi = 3
a.didi
del a.didi

# The above would feel exactly the same way as how python stores and fetches instance
# attributes except that it would prints out the customer message. So, the conclusion
# is that the '__getattribute__', '__setattr__', '__delattr__' methods are ways designed
# to manipulate the python intrinsic descriptor: the '__dict__' desciptor, and you can
# customize it in a similar way as the above example. Below, let's example how this idea
# is extended to customer descriptors.

class Weight(object):
    def __init__(self):
        self.name = 'weight'
        self.all_weight = {}

    def __set__(self, instance, value):
        if not isinstance(value, int):
            print '{} is an invalid {}'.format(value, self.name)
            return
        self.all_weight[instance] = value

    def __get__(self, instance, cls):
        if not self.all_weight.has_key(instance):
            print '{} not have value {}'.format(instance, self.name)
            return
        return self.all_weight.get(instance, None)

    def __del__(self, instance):
        if not self.all_weight.has_key(instance):
            print '{} not have value {}'.format(instance, self.name)
        self.all_weight.pop(instance)

class Color(object):
    def __init__(self):
        self.name = 'color'

    def __get__(self, instance, cls):
        return 'red'

class Dog(object):
    color = Color()
    weight = Weight()

toby = Dog()
toby.weight
toby.weight = '3'
toby.weight = 3
del toby.weight
toby.__dict__
toby.__dict__['weight'] = 5
toby.weight
toby.__dict__['color'] = 'black'
toby.color

"""In the above example, the class Dog has a data descriptor, and a non data descriptor
Descriptors have similar protocol as the python instrinsic getset_descriptor
    __getattribute__ --> __get__
    __setattr__      --> __set__
    __delattr__      --> __del__

    the difference is that instead of manipulating the __dict__ attribute of an object, it
    manipulates the descriptor's own dictionary for keeping info. In our case, its self.all_weight.

And there is such order of checking:
    data descriptor > __dict__ getset descriptor > non data descriptor.

Below is a very detailed proceedure of how python checks for the attributes.

    lili.weight

    1) Dog.__dict__.has_key('weight')? yes --> 2), no --> 3)
    2) Is Dog.weight a
        data descriptor (has __set__ method) --> C
        non data descriptor                  --> 4)
        regular attribute                    --> 5)
    3) lili.__dict__.has_key('weight') yes --> A, no --> B
    4) lili.__dict__.has_key('weight') yes --> A, no --> C
    5) lili.__dict__.has_key('weight') yes --> A, no --> D

    A: return lili.__dict__['weight']
    B: raise AttributeError
    C: return Dog.__dict__['weight'].__get__(lili, Dog)
    D: return Dog.__dict__['weight']

Attribure search only goes one layer up:
    object itself --> its class --> its class's parent classes

Not like:
    object itself --> its class --> its class's class

Some good take away lessons:
    1. The descriptor protocol python offers for customer attributes accessing, assigning works
    exactly in the same way as its builtin __dict__ getset_descriptor.
    assuming:
        class A(object): pass
        lili = A()
    lili.weight would do:
        1) A.__dict__['weight'].__get__(lili, A)  # data descriptor
        2) A.__dict__['__dict__'].__get__(lili, 'weight')

        would do:
        1) A.__dict__['__dict__'].__get__(lili, A)
        2) A.__dict__['weight'].__get__(lili, A)  # non data descriptor

"""
