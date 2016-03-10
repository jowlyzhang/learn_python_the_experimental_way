#!/usr/bin/python
from collections import namedtuple, Counter, OrderedDict

#######################################################
# namedtuple
#######################################################
Point = namedtuple('Point', ['x', 'y', 'z']) # created a named tuple class
a = Point(1, 2, 3)
b = Point(2, 3, 4)
c = (1, 2, 3) # This tuple class can be used similarly as the built_in tuple
d = (2, 3, 4) # data type to initiate an instance

a < b # compare as a regular tuple instance

a[0], a[1], a[2] # normal value access as a regulare tuple

x, y, z = a # unpack as a regular tuple

a.x + a.y + a.z # Bonus: fields accessed as property

e = a._asdict() # Bonus: convert to a dictionary

a = Point(**e) # Bonus: convert from a dictionary

a._replace(x=5) # Bonus: in place change of value with field name


#######################################################
# Counter
#######################################################
c = Counter('abcdeabcedabcde') # Construt a counter from string
c = Counter([1, 2, 3, 4, 2, 2, 3, 4]) # Construct a counter from a list
c = Counter((1, 2, 3, 4, 2, 2, 3, 4)) # Construct a counter from a tuple
c = Counter({'a':3, 'b':3, 'c': 3}) # Construct a counter from a dictionary

sum(c.values()) # Access values as a normal dictionary
sorted(c)  # List unique elements
c['a'] # Access value through key as a normal dict

c.most_common()
c.most_common(2)  # Bonus: list most commonly found element

d = Counter('simsalabim')
c.update(d) # Bonus: update a counter with another counter

#######################################################
# Counter
#######################################################
a = OrderedDict() # As the name indicates, it's ordered, not sorted, so it remembers
                  # order of insertion
a['apple'] = 3
a['pear'] = 4
a['watermelon'] = 5
print a.keys()
a.popitem() # For ordered stuff, you are able to pop it.
