"""This module is a demonstration for the xunit-like fixture features that pytest offers.
Like unittest, pytest supports shared setup, teardown feature, even to a better defined
granunarity, the level of fixtures offered including module level, function level, class
level, method level. The only draw back is that it involves some code changes when a test
method (function) doesn't share setup or teardown fixturess with other tests. You basically
needs to isolate that test into a separate class to provide it with better defined setup
and teardown. In another file, a pytest style fixture feature will be introduced to better
solve this issue.
"""
def setup_module():
    print 'Testing whole module started'

# This is the shared setup function for all module level test functions.
# Cannot change this function name. It's called before calling any module
# level test function with the function pointer as an argument.
def setup_function(func):
    print 'Shared test setup for test {}'.format(func.__name__)

def test_8():
    assert 8 == 8

def test_9():
    assert 9 == 9

# This is the shared teardown function for all module level test functions.
# Cannot change this function name. It's called after calling any module
# level test function with the function pointer as an argument.
def teardown_function(func):
    print 'Shared test teardown for test {}'.format(func.__name__)

def teardown_module():
    print 'Testing whole module finished'


class TestMe():
    def setup_class(cls):
        print 'Start testing the whole class'

    # This setup function is also a shared one, it's called after the setup_method
    # is called for each test method.
    def setup(self):
        print 'The standalone setup function in the class'

    def setup_method(self, method):
        print 'Shared test setup for test {}'.format(method.__name__)

    def test_me(self):
        assert 'Apple' is 'Apple'

    def test_him(self):
        assert 'Pear' is 'Pear'

    def teardown_method(self, method):
        print 'Shared test teardown for test {}'.format(method.__name__)

    def teardown_class(cls):
        print 'Finish testing the whole class'

    def teardown(self):
        print 'The standalone teardown function in the class'
