from constants.settings import DRIVER


class SeleniumWrapper(object):

    # singleton
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SeleniumWrapper, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def getDriver(self):
        self.driver = DRIVER
        return self.driver
