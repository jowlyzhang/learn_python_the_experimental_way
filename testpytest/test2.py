import pytest

# This is a cool feature that is also more self-explainatory.
# 1. The teardown code is tightly coupled up with the setup code of a resource.
# 2. The lifescope of a resource is obvious.
# 3. It's obvious which tests are running on a resource.
# 4. Don't need to group tests into classes to differetiate use of resources.
# Optional keywords for the fixture object.
# scope (str): 'function', 'module', 'class', 'session' specifies the life span of this fixture.
# params (list): parameterize tests that uses this fixture.
# autouse (bool): Default to False which means whichever test that wishes to use this test fixture
# needs to specify it either by adding the mark.usefixtures decorator or add the fixture in the
# argument list. If it's set to True, all tests in the session would use this fixture aotomatically.
# this is a powerful feature that could be useful in some cases but it does come with a great
# impact.
@pytest.fixture(scope='function', params=[1, 2, 3])
def resource_a(request):
    print 'Setting up resource a'
    print '\n---------------------'
    print 'fixturename: {}'.format(request.fixturename)
    print 'scope: {}'.format(request.scope)
    print 'function: {}'.format(request.function.__name__)
    print 'cls: {}'.format(request.cls)
    print 'module: {}'.format(request.module.__name__)
    print 'fspath: {}'.format(request.fspath)
    print '\n---------------------'
    return request.param
    def resource_teardown():
        print 'Teardown a resouce'
    request.addfinalizer(resource_teardown)

@pytest.fixture(scope='function')
def resource_b(request):
    print 'Setting up resource b'

def test_without_resource():
    print 'This test does not require resource'


def test_without_resource2():
    print 'This is another test that does not require resource'

# Below are the two forms of adding a fixture to a test, either by using the
# pytest.mark.usefixtures decorator or pass a pytest.fixture object as an argument
# for a test. Each of this would create a request object to be passed to the fixture.
def test_with_resource(resource_a):
    print 'This test requires resource'
    print resource_a

@pytest.mark.usefixtures('resource_b')
def test_with_resource2():
    print 'This test also requires resource'

# The add fixtures as test parameters feature make it easy and readable to add multiple fixtures to
# one test. As an alternative, we can chain multiple fixtures together to achieve the same thing.
def test_with_resource3(resource_a, resource_b):
    print 'This test requires both resources'

#######################################################################
"""if issubinstance(func_arg, pytest.fixture):
    request = Request()
    request.function = func
    request.cls = None of cls
    request.module = func.__module__ or cls.__module__
    request.scope = func_arg.scope

func_arg(request)


def fixture(scope='function', params=None, autouse=False):
    def func_wrap_helper(func):
        def new_func(request):
            if params is not None and isinstance(params, list):
                param = next(params)
            else:
                param = None

            return func(request)
        return new_func
    return func_wrap_helper"""


