import copy

from base_page_element import BasePageElement
from pypop.pageobjects import SeleniumWrapper


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

        if 'url' in attrs:
            instance.url = copy.deepcopy(attrs['url'])

        return instance


class PageObject(object):
    """
    The purpose of the metaclass is to prepare our instance, right when it
    is created. For example it will clone all the attributes of the class
    that inherit from BasePageElement, and also these to the newly created
    class instance.
    """
    __metaclass__ = BasePageObjectMeta

    def __new__(cls,  *args, **kwargs):
        ret = super(PageObject, cls).__new__(cls, *args, **kwargs)
        ret.driver = SeleniumWrapper().getDriver()
        return ret

