# coding=utf-8

import unittest
import uuid
import random
import datetime
import time
import string
import pprint

from selenium.webdriver.common.by import By

from pypop.pageobjects.base_page_object import PageObject
from pypop.pageobjects.base_page_element import InputField, PasswordField, Button

import os.path


class LoginPageObject(PageObject):
    url = 'file://' + os.path.abspath(os.path.join(os.path.dirname(__file__), 'login.html'))
    username = InputField((By.ID, 'username'))
    password = PasswordField((By.ID, 'password'))
    btn_login = InputField((By.ID, 'btn-login'))

    def goTo(self):
        self.driver.get(self.url)


class TestLogin(unittest.TestCase):
    """
    Here we test the address book functionality.
    """
    def setUp(self):
        self.loginPage = LoginPageObject()
        self.loginPage.goTo()

    def test_login_success(self):
        """
        """
        self.loginPage.username = "test"
        self.loginPage.password = "secret"
        self.loginPage.btn_login.click()


if __name__ == "__main__":
    unittest.main()

    # from selenium import webdriver
    # from selenium.webdriver.common.keys import Keys

    # driver = webdriver.Firefox()
    # driver.get("file:///Users/nutrina/Projects/personal/pypop/pypop/example/ex1/login.html")
    # elem = driver.find_element_by_id("username")
    # print elem
