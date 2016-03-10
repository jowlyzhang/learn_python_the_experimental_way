#!/usr/bin/python
"""This experiment is about the __weakref__ attribute of a class.
The __weakref__ attribute of a class is of type getset_descriptor
the same as the __dict__ attribute of a class as experimented in
cls_attr2.py. """
import weakref

class God(object):
    def __init__(self, name):
        self.name = name

lilith = God('lilith')
adam = God('adam')

eva0 = weakref.proxy(adam)
eva1 = weakref.proxy(lilith)

print God.__weakref__.__get__(lilith, God)
print weakref.getweakrefs(lilith)
print God.__weakref__.__get__(lilith, God).name
print lilith.__weakref__.name

print God.__weakref__.__get__(adam, God)
print weakref.getweakrefs(adam)
print weakref.getweakrefcount(adam)
print God.__weakref__.__get__(adam, God).name

eva2 = weakref.proxy(adam)
print God.__weakref__.__get__(adam, God)
print weakref.getweakrefs(adam)
print weakref.getweakrefcount(adam)
print God.__weakref__.__get__(adam, God).name

del eva0
print God.__weakref__.__get__(adam, God)
print weakref.getweakrefs(adam)
print weakref.getweakrefcount(adam)
print God.__weakref__.__get__(adam, God).name
