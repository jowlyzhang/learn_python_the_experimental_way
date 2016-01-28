class MyObject():
    def __init__(self):
        pass

    def __new__(self):
        pass

    def __delattr__(self):
        pass

    def __getattribute__(self):
        pass

    def __setattr__(self):
        pass

    def __dict__(self):
        pass

    def __hash__(self):
        pass

    def __class__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __format__(self):
        pass

    def __reduce__(self):
        pass

    def __reduce_ex__(self):
        pass

    def __sizeof__(self):
        pass

    def __weakref__(self):
        pass

    def __subclasshook__(self):
        pass


if __name__ == '__main__':
    print dir(MyObject)
