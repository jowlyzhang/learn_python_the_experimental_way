class type():
    @classmethod
    def __call__(meta_cls, name=None, bases=None, nmspc=None):
        # meta_cls = type
        if not meta_cls:
            raise TypeError()

        if name and bases and nmspc:
            # create an object with inheritance tree.
            meta_cls = scoop_a_chunk_of_memory()
            link_it_to_its_ancesters(meta_cls)
            add_to_it_its_namespace(meta_cls)
            return meta_cls
        else:
            # create an simple object



class MetaA(type):
    # below is inherited, just type out to show details, donot actually define
    # MetaA('classA', (), {})
    @classmethod
    def __call__(meta_cls, name=None, bases=None, nmspc=None):
        # meta_cls = MetaA
        if not meta_cls:
            raise TypeError()

        if name and bases and nmspc:
            cls = 




class object():

    # below is override of the type's __call__
    @classmethod
    def __call__(cls):
        # cls = object
        new_instance = type.__call__(cls)


class ClassA(object):
    #below is inherited, just type out ot show details, donot actually define
    @classmethod
    def __call__(cls):
        # cls = ClassA
        new_instance = type.__call__(cls)
