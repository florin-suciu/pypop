from pypop.pageobjects import seleniumWrapper


class BasePageElement(object):

    def __init__(self, locator_info):
        self.by, self.locator = locator_info
        self.driver = seleniumWrapper.getDriver()

    def __set__(self, obj, val):
        self.driver.find_element(self.by, self.locator).send_keys(val)

    def __get__(self, obj, cls=None):
        return self.driver.find_element(self.by, self.locator).get_attribute('value')

    def __delete__(self, obj):
        pass


class BasePageElementClearFirst(object):
    """
    Why not simply use a clear flag on BasePageElement ?
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
