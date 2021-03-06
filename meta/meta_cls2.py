#!/usr/bin/python
"""Meta classes are created by 'type', classes are also created by 'type'. Class
objects are created by 'object'. The simplest case, not any customerization:
not only is metaclass created by 'type', it also inherites all the good methods that
type has.
    >>> class MyMeta(type): pass
    >>> MyMeta = type('MyMeta', (type, ), {})
    >>> class MyClass:
            __metaclass__ = MyMeta

    >>> MyClass = MyMeta('MyClass', (), {})
    >>> MyClass.__class__
    >>> MyMeta
    >>> MyClass = type.__new__(MyMeta, 'MyClass', (), {})
    >>> MyClass.__class__
    >>> MyMeta

    >>> MyMeta.__new__ = type.__new__ # Classes created by type
    >>> True
    >>> MyClass.__new__ = object.__new__ # Class objects created by object
    >>> True

    >>> type.__class__ = type
    >>> type.__class__.__new__ = type.__new__
    >>> type.__base__.__new__ = object.__new__
    >>> object.__base__ == None

Attach a figure.
"""
class MyMeta(type):
    pass

# is egual to
MyMeta = type.__new__(type, 'MyMeta', (type,), {})

# To add some customerization, don't forget call type.__new__
# Customerization can be fulfilled in the __init__ method most likely

class MyMeta(type):
    def __new__(meta_cls, *args, **kwds):
        # It looks like in the __new__ function of type, it will call
        # the __init__ function of the class at some time, don't need
        # to specifically call it.
        cls = type.__new__(meta_cls, *args, **kwds)
        print cls
        type(cls)
        cls.__class__
        # This one won't work, looks like it's not passing the object class to bound
        #cls.__init__(*args, **kwds)
        # This one works even though it't not required
        meta_cls.__init__(cls, *args, **kwds)
        return cls

    def __init__(cls, name, bases, dct):
        print 'Customer metaclass'
        type.__init__(cls, name, bases, dct)
        cls.uses_metaclass = lambda self: 'yes'

class MyClass(object):
    pass

# is equal to

MyClass = type('MyClass', (), {})

class MyClass(object):
    __metaclass__ = MyMeta

# is equal to
MyClass = MyMeta('MyClass', (object,), {})

# To add some customerization, don't forget to call object.__new__

class MyClass(object):
    __metaclass__ = MyMeta
    def __new__(cls, *args, **kwds):
        self = object.__new__(cls)
        print self
        type(self)
        self.__class__
        # Below lines both work even though it's not needed.
        MyClass.__init__(self, *args, **kwds)
        self.__init__(*args, **kwds)
        return self

    def __init__(self, *args, **kwds):
        print 'customer class'
        print 'I got args: {}'.format(args)
        print 'I got kwds: {}'.format(kwds)

"""
At the end of this metaclass journey, it turned out there are bigger doors open
to understand even more about python's object oriented working mechanism, other
than just understanding the meta class mechanism. Let's tell it as a story.
There is a guy named `type`, when he get a request from someone that they want
to create an object, he asks.
    1. 'what name do you want to give to this object?', he got it, then he asked
    2. 'should this object be in any inheritance relationship with other objects?'
    3. 'what property does this object have in hand?'

    After he got the answers, he has two magic tools to help him make this object.
    1. The first one is called `__new__`, he uses this guy to scoop a chunk of space from
    the memory to store this object.

    let's assume calling type.__new__(cls_name, *args, **kwds) is equivalaent of calling the C
    function that deals with memory and scoop such a chunk for us

    a chunk of memory space is scooped by C function whenever one of the following things happen:
        1. class SomeName(type):
           some variable inherites 'type', which makes it a metaclass
        2. class SomeName:  or
           class SomeName(object):  or
           class SomeName:
               __metaclass__ = SomeMetaClassName  or
           class SomeName(object):
               __metaclass__ = SomeMetaClassName

           Some class variable is defined, it either has or doesn't have a customized metaclass.

    a chunk of memory space is scooped by python function when you do
        3. SomeName = OtherName()  where OtherName has a '__new__' method in its namespace

    remeber that the '__new__' and '__init__' method you defined for a metaclass or a class
    is defining the actions for creating its respective objects, not for creating itself.

    2. The second one is called `__init__`, which he uses to do some extra decoration
    for this object.

    3. He also do some extra stuff, like link this guy with the other objects he should
    be linked with, which may involve some computation of path to get to those objects.
He then returns this object to whoever asks for it.

There are some guys out their that also wants to have type's magic power of creating
an object. So these guys declare that they are type's kids. They are called metaclass
By being type's kids, they automatically have all the power that type has, because they
can always ask type to do it for them and they can even augument if they want.
They can create an object upon requests too. These guys can take over type's role as
a factory for classes.

But people notices that the class object created by metaclass can also create an object
upon requests too. Themselves serve as a factory for creating instances, how could that
happen? Only guys who have the magic power of 'scooping' memory space and `decorating`
it has the power to create objects. type's kids have that power, but why are these
class objects also have that power. It turned out another guy called `object` also has
similar power.`object` is not type's kid, he doesn't inherit anything from type. But
when you ask object something about his identity, he says he's related to type. He also
has the magic of 'scooping' memory and decorate it, but his specialization is different.
He gets called at different times and asks different questions. type gets called when
a class object is created in the code or when get called explicitely for such purpose.

When python sees something like this: a(*args, **kwds), he asks a
    1. Do you have a __call__ method? if not, looks like you are a little nobody
    2. Does your __class__ object has a __call__ method ? if not
    2. Does your __class__ object's father have a __call__method? if not keep asking
    3. Does your __class__ object's grandfather have a __call__method?

When it comes to the __call__ method of its class, it will do a.__class__.__call__(a, *args, **kwds)

When it comes all the way to Mr object. And python tell Mr object that somebody called you
with this *args, *kwds, please take it and give me something, I will return whatever you give
me to that someone. So Mr object would ask __new__ to scoop a chunk of memory, and ask __init__
if he wants to do something extra and return that thing to python.

When it comes all the way to Mr Type, Python tell Mr Type that somebody is trying to call
you with this *args, **kwds, please take it and give me something. Mr type take a look at
this args and kwds and asks?
    1. What nametag does this someone want me to put on the thing I created?
    2. What is this thing's ancesters? Nothing? ok, I'll make `object` its dad
    3. Is there anything available right now to put into the object I created?
If python cannot give answers that follow Mr types format, Mr type would simply not do it.
Metaclass defines customized class definition, class defines customized
objects definition.
It usually suffice to put your customization in the __init__ method unless
you want to interfer witht the memory allocation process.
Metaprogramming is aiming at using a class factory that dynamically
create classes for use in the same way that class instances are created.
The factory for class instances are class themselves. Similarly, the
factory for class creation is metaclass. The default metaclass in python
is `type`, all the builtin classes, including data types, functions and
user defined classes are of class `type`. This is easily experimented.
Try in a python interpreter.
>>> type(int)
    def my_func():
        pass
    my_func.__class__.__class__
    class MyClass():
        pass
    MyClass.__class__

You can think of defining a customer class as calling the `type` function
with base class, namespace dict and class name at interpretation time. That
is the usual way of creating a class, using the `type` metaclass. Python
allows for a metaclass hook that can change the metaclass a class creation
is based on. This is done by providing the metaclass hook as a static field
called `__metaclass__` in the class definition.
After the initial creation of the class object. it will call __metaclass__()
with class object, class name, bases, and namespace dictionary, I created the
below Myclassmethod to provide a customerized way of providing the `__metaclass__`
hook and it shows that __metaclass__ hook is not called as a classmethod.

Let's prototype what the __new__ and __init__ methods of the `type` class should be
like
>>> class type:
        def __new__(type, *args, **kwds):
            cls_instance = allocate_space_and_create_object(*args, **kwds)
            cls_instance.__init__(*args, **kwds)
            return cls_instance
        def __init__(instance, *args ,**kwds):
            manipulate(instance)

Let's also prototype what `object` class should be like:
>>> class object:
        def __new__(object, *args, **kwds ):
            object_instance = allocate_space_and_create_object(*args, **kwds)
            object_instance.__init__(*args, **kwds)
            return object_instance
        def __init__(object_instance, *args, **kwds):
            manipulate(object_instance)
"""
import pdb

class MyMeta(type):
    def __new__(meta_cls, *args, **kwds):
        cls = type.__new__(meta_cls, *args, **kwds)
        cls.__init__(*args, **kwds)
        return cls

    def __init__(cls, name, bases, dct):
        super(MyMeta, cls).__init__(name, bases, dct)
        # equal to:
        # type.__init__(cls, name, bases, dct)
        cls.uses_metaclass = lambda self: "yes!"

def funcMeta(name, bases, nmspc):
    cls = type.__new__(type, name, bases, nmspc)
    cls.uses_metaclass = lambda self: "yes!"
    return cls


# The usual way of adding a metaclass. use the __metaclass__ hook
# to point to a metaclass that inherites `type`
class FirstClass():
    __metaclass__ = MyMeta

# But it turned out that the __metaclass__ hook doesn't necessarily
# have to point to a metaclass that inherites `type`. It just has
# to be a callable and returns a class object.
class SecondClass():
    __metaclass__ = funcMeta

# And this callable function can be used to directly return
# the class object
ThirdClass = funcMeta('ThridClass', (object,), {})

# The same for the metaclass that inherites `type`
FourthClass = MyMeta('FourthClass', (object,), {})

class Myclassmethod(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        self.instance = instance
        self.cls = cls
        return self

    def __call__(self, *args, **kwds):
        return self.func(*args, **kwds)

# This is for showing the syntax of adding __metaclass__ as a static field
# is nothing more than adding a classmethod field.
class FifthClass():

    @Myclassmethod
    def __metaclass__(*args, **kwds):
        return MyMeta(*args, **kwds)

    def foo(self): pass

    @staticmethod
    def bar(): pass

"""To sum the above up, usually, class objects are generated by the type class
by either defining it in the code without adding any __metaclass__
hook or explicitely calling the type() function with name, bases and dct.
Note that this is basically the samething as define class in the code, it could
be assumed that working mechanism of defining a class in the code works as this:
    when python interpreter encounters a line of code like this:
        >>> class Something(BaseSomething, BaseAnotherthing):
                some_variable = ''
                def some_func(self):
                    pass

a.it will be parsed to come up with these things:
        1. name: 'Something'
        2. bases: (BaseSomething, BaseAnotherthing, )
        3, nmspc: {'some_variable': '';
                   'some_func': <function object>}

b. is there a __metaclass__ field defined in the nmspc?
        1. Nope -> do:
            >>> Something = type(name, bases, nmspc)

        2. Yes -> do:
            >>> Something = Something.__dict__['__metaclass__'](name, bases, nmspc)

        hopefully, this callable __metaclass__ hook would create a class object and return it.
        There are two ways of doing it:
            1. if __metaclass__ hooks to a function, that function would be called with(name, bases, nmspc)
               in the function body, create a class object and return it using either
               return type(name, bases, nmspc) or type.__new__(type, name, bases, nmspc) which are
               essentially the same thing. And Something.__class__ would be type.

            2. if __metaclass__ hooks to a metaclass that inherites from `type`. The type.__new__ function
               will be called automitically and that should do it. You can override __new__ and __init__
               functions to make it more customized, but don't miss creating a class object and return it.

c. It should be of interest to think about what type.__new__ do after it gets the (type, name, bases, dict)
arguments. Here is a break down of the arguments.
    1. type: this could be type or a metaclass that inherites from type. Anyway, it has to be a
    metaclass.
    2. name: name of the class, it's beneficial and convential to make it the same as the variable name
    that points to this class object.
    3. bases: the base classes of this class
    4. dict: the current namespace this class has.
The purpose of having inheritance is for attribute sharing. and type.__new__ only need to have references
pointing to its ancestors for later reference.

Now here comes things that are even more tricker:
    how does the metaclass definition process follow the above procedure for defing a class.Do:
"""
# The following two lines of code does exactly the same thing where `type` work as
# both: the metaclass for creating the metaclass object `MetaCls`, and also its
# Ancestor
MetaCls = type('MetaCls', (type, ), {})
MetaCls = type.__new__(type, 'MetaCls', (type, ), {})
MyClass = MetaCls('MyClass', (), {})

# If taking out the ancestor part and do:
MetaCls = type('MetaCls', (), {})
# It would be a `type` object and you won't be able to:
try:
    MyClass = MetaCls('MyClass', (), {})
except TypeError:
    pass

"""To sum up:
    1. if `A` inherits from type. It would be a metaclass. And you will be able to
    call newclass = A('newclass', (), {}) which in turn calls:
        a. newclass = type.__call__('newclass', (), {})
        b. -> cls = A.__new__('newclass', (), {}), A.__init__(cls, *args, **kwds)
        c. return cls
    and then when you create a new object by mo = newclass(*args, **kwds), it in turn calls:
        a. -> self = newclass.__new__(*args, **kwds), newclass.__init__(*args. **kwds)
        b. it defaults to self = object.__new__(*args, **kwds), object.__init(*args ,**kwds)
        c return self

    and then when you do mo(*args, **kwds), it in turn calls:
        a. return newclass.__call__(mo, *args, **kwds)

    2. if `A` is a `type` object. It is not a metaclass. And doing
    newinstance = A(*args, **kwds) would call:
        a. newinstance = A.__call__(*args, **kwds)
        b. -> self = A.__new__(*args, **kwds), A.__init__(self, *args, **kwds)
        c.return self

"""


class Event(object):
    events = []

    def __init__(self, action, time):
        self.action = action
        self.time = time
        Event.events.append(self)

    def __cmp__(self, other):
        return cmp(self.time, other.time)

    def run(self):
        print"%.2f: %s".format(self.time, self.action)

    @staticmethod
    def run_events():
        Event.events.sort()
        for e in Event.events:
            e.run()


def create_mc(description):
    # Dynammically create a class by using the type function, provided its
    # class name, base class tuple, and namespace dictionary. Type function
    # would return a class object, and we need to add it to the global namespace
    # to be able to access it.
    class_name = "".join(x.capitalize() for x in description.split())
    def __init__(self, time):
        Event.__init__(self, description + " [mc]", time)

    globals()[class_name] = type(class_name, (Event,), dict(__init__=__init__))


def create_exec(description):
    # Dynamically create a class by executing a string that defines a class
    # and add it to global namespace
    class_name = "".join(x.capitalize() for x in description.split())
    klass = """
class %s(Event):
    def __init__(self, time):
        Event.__init__(self, "%s [exc]", time)
    """ % (class_name, description)
    exec klass in globals()


if __name__ == '__main__':
    descriptions = [
        'Light On',
        'Light Off',
        'Water On',
        'Water Off',
        'Thermostat night',
        'Thermostat day',
        'Ring bell',
    ]
    initializations = "ThermostatNight(5.00); LightOff(2.00);\
        WaterOn(3.30); WaterOff(4.45); LightOn(1.00);\
        RingBell(7.00); ThermostatDay(6.00)"

    # Create a class for each description that inherites from class
    # `Event` and add it to the global namespace
    [create_mc(dsc) for dsc in descriptions]
    exec initializations in globals()
    [create_exec(dsc) for dsc in descriptions]
    exec initializations in globals()
    Event.run_events()


class MyMeta(type):
    pass

# is egual to
MyMeta = type.__new__(type, 'MyMeta', (type,), {})

# To add some customerization, don't forget call type.__new__
class MyMeta(type):
    def __new__(meta_cls, *args, **kwds):
        cls = type.__new__(meta_cls, *args, **kwds)
        cls.__init__(*args, **kwds)
        return cls

    def __init__(cls, name, bases, dct):
        print 'Customer metaclass'
        type.__init__(cls, name, bases, dct)
        cls.uses_metaclass = lambda self: 'yes'

 class MyClass(object):
     __metaclass__ = MyMeta

 # is equal to
MyClass = MyMeta('MyClass', (object,), {})

# To add some customerization, don't forget to call object.__new__

class MyClass(object):
    __metaclass__ = MyMeta
    def __new__(cls, *args, **kwds):
        self = object.__new__(cls)
        self.__init__(*args, **kwds)
        return self

    def __init__(self, *args, **kwds):
        print 'customer class'
        print 'I got args: {}'.format(args)
        print 'I got kwds: {}'.format(kwds)



