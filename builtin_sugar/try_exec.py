#!/usr/bin/python
cf = open('exec_test.txt', 'r')
exec(cf)

def func(a):
    print a

# eval executes the python code represented by the string and return its return value
eval("func(6)")
# exec only executes the python code represented by the string
exec("func(6)")

code_str = """
def func1(a):
    print a
    return a
"""

# eval cannot eval a non-expression statement
code_str1 = """
print 'bulala'
"""

code_str2 = """
a = [1, 2, 3]
"""
# eval can evaluate an expression
code_str3 = """
map(lambda x: str(x), range(0, 6))
"""

# eval cannot evaluate multiple expression
code_str4 = """
#map(lambda x: str(x), range(0, 6))
#[1, 2, 3]
{'a':3, 'b': 4}
"""
exec(code_str4)
eval(code_str4)
"""Every line of code in python is a statement, including but not limited to:
    1. a = 6, assignment statement
    2. return 6, returing statement
    3. def func(a): function definistion statement
    4. if a == 6: conditional statement
    5 print 'bulala' printing statement
    6 func(3), function calling statement.
    7 [str(x) for x in range(0, 6)] list comprehension statement.

of all statements only those that can reduce to one python object is an expression.
Among the above listed ones, only 6 and 7 are expressions.
"""
