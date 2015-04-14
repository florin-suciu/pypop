# coding=utf-8

import unittest
import uuid
import random
import datetime
import time
import string
import pprint

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from pypop.pageobjects.base_page_object import PageObject
from pypop.pageobjects.base_page_element import InputField, PasswordField


class LoginPageObject(PageObject):
    username = InputField()
    password = PasswordField()


class TestAddressbook(unittest.TestCase):
    """
    Here we test the address book functionality.
    """
    def setUp(self):
        self.loginPage = LoginPageObject()

    def test_login_success(self):
        """
        """
        self.loginPage.username = "test"
        self.loginPage.password = "secret"
        self.loginPage.login.click()


if __name__ == "__main__":
    unittest.main()
