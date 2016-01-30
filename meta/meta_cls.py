#!/usr/bin/python
"""Customer defined classes are objects too.
Class is the template for creating class instances. So
what are the templates for defining classes.
Everying named variable in python is a 'first class' object.
which means class is also one, check out the code below.
"""

class Dog(object):
    def eat(self):
        print "eating"

class BigDog(Dog):
    def eat(self, a):
        print "eating"*a

def bark(self):
    print "wangwangwang"

def sleep():
    print "wululu~~wulululu~~"


if __name__ == "__main__":
    lili = BigDog()
    try:
        lili.eat()
    except TypeError:
        print "Python won't check your argument list for you, Be an adult, man!"

    try:
        lili.bark()
    except AttributeError:
        print "Sorry, I'm a friendly-not-barking dog "

    setattr(BigDog, 'bark', bark)
    try:
        lili.bark()
    except:
        print "still not barking"
    else:
        print "I'm old enough to bark, mommy!"

    setattr(BigDog, 'sleep', sleep)
    try:
        lili.sleep()
    except:
        print "Python automatically pass me to sleep, but it does not take me, oh, Man, I have insomnia"
