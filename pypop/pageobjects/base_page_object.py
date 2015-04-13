from base_page_element import BasePageElement


class BasePageObjectMeta(type):
    """
    Metaclass for all PageObjects.
    """
    def __new__(cls, name, bases, attrs):
        instance = super(BasePageObjectMeta, cls).__new__(cls, name, bases, attrs)

        #
        # We clone all the attributes of class that inherit BasePageElement, and
        # we add these as attributes of the instance
        for name, value in attrs.iteritems():
            if isinstance(value, BasePageElement):
                setattr(instance, name, copy.deepcopy(value))

        return instance


class PageObject(BasePageObject):
    """
    The purpose of the metaclass is to prepare our instance, right when it
    is created. For example it will clone all the attributes of the class
    that inherit from BasePageElement, and also these to the newly created
    class instance.
    """
    __metaclass__ = BasePageObjectMeta
