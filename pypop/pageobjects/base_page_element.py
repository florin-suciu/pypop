from pypop.pageobjects import SeleniumWrapper


class BasePageElement(object):

    def __init__(self, locator_info):
        self.by, self.locator = locator_info

    @property
    def driver(self):
        """
        Driver is a property. We always get driver from the SeleniumWrapper.
        the driver should not be stored in an attribute:
          self.driver = ....

        because the cloning will also clone a new driver - this will cause errors & confusion.
        """
        return SeleniumWrapper().getDriver()

    @property
    def element(self):
        """Returns the selenium element."""
        return self.driver.find_element_by_id(self.locator)

    @property
    def value(self):
        return self.element.get_attribute('value')

    def __set__(self, obj, val):
        self.element.send_keys(val)

    def __delete__(self, obj):
        pass

    def click(self):
        self.element.click()


class BasePageElementClearFirst(object):
    """
    TODO: Why not simply use a clear flag on BasePageElement ?
    """
    def __init__(self, locator_info):
        self.by, self.locator = locator_info

    def __set__(self, obj, val):
        element = self.driver.find_element(self.by, self.locator)
        element.clear()
        element.send_keys(val)

    def __get__(self, obj, cls=None):
        return self.driver.find_element(self.by, self.locator).get_attribute('value')

    def __delete__(self, obj):
        pass


class InputField(BasePageElement):
    pass


class PasswordField(BasePageElement):
    pass


class Checkbox(BasePageElement):
    pass


class Select(BasePageElement):
    pass

class Button(BasePageElement):
    pass
