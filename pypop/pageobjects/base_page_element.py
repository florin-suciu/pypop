import unittest

from pypop.pageobjects import selenium_server_connection as ssc


class BasePageElement(unittest.TestCase):

    def __init__(self, locator_info):
        self.by, self.locator = locator_info

    def __set__(self, obj, val):
        ssc.driver.find_element(self.by, self.locator).send_keys(val)

    def __get__(self, obj, cls=None):
        return ssc.driver.find_element(self.by, self.locator).get_attribute('value')

    def __delete__(self, obj):
        pass


class BasePageElementClearFirst(unittest.TestCase):

    def __init__(self, locator_info):
        self.by, self.locator = locator_info

    def __set__(self, obj, val):
        element = ssc.driver.find_element(self.by, self.locator)
        element.clear()
        element.send_keys(val)

    def __get__(self, obj, cls=None):
        return ssc.driver.find_element(self.by, self.locator).get_attribute('value')

    def __delete__(self, obj):
        pass
