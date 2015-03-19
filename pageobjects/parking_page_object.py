from constants.common import PARKING_TITLE, PARKING_URL

from pageobjects.base_page_element import BasePageElement, BasePageElementClearFirst
from pageobjects.base_page_object import BasePageObject
from pageobjects import locators

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ParkingCalculatorPageObject(BasePageObject):

    lot = BasePageElement('parking.lot')
    start_time = BasePageElementClearFirst('parking.entry_time')
    start_date = BasePageElementClearFirst('parking.entry_date')
    end_time = BasePageElementClearFirst('parking.exit_time')
    end_date = BasePageElementClearFirst('parking.exit_date')

    def __init__(self, driver):
        self.driver = driver
        try:
            self.assertEqual(PARKING_TITLE, self.driver.title)
        except AssertionError:
            self.driver.get(PARKING_URL)
            self.assertEqual(PARKING_TITLE, self.driver.title)

    def calculate(self):
        locator, by = locators.get("parking.calculate")
        calculate_button = self.driver.find_element(by, locator)
        calculate_button.click()

    def check_value(self):
        time_locator, time_by = locators.get("parking.result_time")
        price_locator, price_by = locators.get("parking.result_price")

        a = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((time_by, time_locator)))

        time_element = self.driver.find_element(time_by, time_locator).get_attribute('value')
        price = self.driver.find_element(price_by, price_locator).get_attribute('value')

        # TODO: continue check after setting the locators right
