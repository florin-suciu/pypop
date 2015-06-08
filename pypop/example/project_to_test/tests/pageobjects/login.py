import os

from selenium.webdriver.common.by import By

from pypop.pageobjects.base_page_object import PageObject
from pypop.pageobjects.base_page_element import InputField, PasswordField


class LoginPageObject(PageObject):
    '''Page object for the login page'''
    url = 'file:///' + os.path.dirname(__file__) + '/../../login.html'
    username = InputField(By.ID, 'username')
    password = PasswordField(By.ID, 'password')
    btn_login = InputField(By.ID, 'btn-login')

    def go_to(self):
        self.driver.get(self.url)
