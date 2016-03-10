# Before working on weak reference, let's see first what does a strong reference
# mean.

# Create a python list object and have two variables refer to it
a = [1, 2, 3]
b = a # Assignment is strong reference

# The created list object doesn't get deleted until all strong references pointing
# to it end lifespan
del a
del b

# This can be more obvious for a class that has a explicit __del__ function

class ExampleObject(object):
    def __init__(self):
        self.obj = None
        print 'object created'

    def store(self, obj):
        self.obj = obj

    def show(self):
        print self.obj

    def __del__(self):
        print 'object deleted'

a = ExampleObject()
b = a
del b
del a

import weakref
# Weak reference on the other hand doesn't affect the reference count of an object
# and an object with only weak references would be destroyed. Namely, weak reference
# won't impede object destruction.

# To create a weak reference to an object
a = ExampleObject()
b = weakref.ref(a) # First argument to this function call is a strong reference to an object, and
                   # it returns a weak reference

print 'Equal: {}'.format(a == b()) # Calling a weak reference would create a temporary strong reference
del a # Deleting the only strong reference to an object would cause it to be destructed

b() is None # Calling a weak reference after object has been destroyed would return None

a = ExampleObject()
b = weakref.proxy(a) # This function takes a strong reference and returns a weak reference proxy 

b.store('fish') # A weak reference proxy works the same as a strong reference

del a

b.show() # Except that it throws a ReferenceError after a target is dead

# Above is how a weak reference work and below let's start talk about how it can be used.

# When two objects have cyclic references, they cannot be deleted until interpreter exits.
# Cyclic references can be common in a some applications, when child instance refers to mother
# and mother refers to child. In singly-linked list and doublely-linked list, it can be common
# too.
a = ExampleObject()
b = ExampleObject()
a.obj = b
b.obj = a
del a
del b

# The solution is to implement weak reference. This way, object is destructed as long
# as the strong reference is deleted
class WeakExample(ExampleObject):
    def store(self, obj):
        self.obj = weakref.proxy(obj)

# Weak reference cannot be created for builtin types like list, tuple, dictionary for obvious
# reasons. It would raise a TypeError. There are other times when weak reference cannot be
# created and failed silently
a = WeakExample()
b = WeakExample()
a.store(b.show)
a.show()
# It shows None instead of the expected bound method. The reason for this is a.store(b) would
# pass strong reference b to the WeakExample object to show, it creates a weak reference to
# that object  and stores it in a.obj, but a.store(b.show) would create a bound function on
# demand and pass it to a.obj, but when the function call ends, the bound function created
# on demand is also destructed, thus a.obj reference to a dead target.
