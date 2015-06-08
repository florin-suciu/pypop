from pypop.pageobjects import SeleniumWrapper


class BasePageElement(object):

    def __init__(self, by, locator, clear=False):
        self.by = by
        self.locator = locator
        self.clear = clear

    @property
    def driver(self):
        """Driver is a property. We always get driver from the SeleniumWrapper. The driver should not be stored in an
        attribute because the cloning will also clone a new driver - this will cause errors & confusion.
        """
        return SeleniumWrapper().getDriver()

    @property
    def element(self):
        """Returns the selenium element."""
        return self.driver.find_element(self.by, self.locator)

    @property
    def value(self):
        return self.element.get_attribute('value')

    def __set__(self, obj, val):
        if self.clear:
            self.element.clear()
        self.element.send_keys(val)

    def __delete__(self, obj):
        pass

    def click(self):
        self.element.click()


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
