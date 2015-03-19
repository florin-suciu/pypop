import unittest
import logging

from pageobjects.parking_page_object import ParkingCalculatorPageObject
from pageobjects import selenium_server_connection

from constants.settings import LOG_PATH


class TestParkingCalculator(unittest.TestCase):

    def setUp(self):
        self.log = logging.getLogger(LOG_PATH)
        self.log.info("TestParking setup")
        self.verificationErrors = []
        self.driver = selenium_server_connection.getDriver()

    def tearDown(self):
        self.log.info("TestParking setup")
        self.driver.close()
        self.assertEqual([], self.verificationErrors)

    def test1(self):
        self.log.info("Running test test1")
        pcpo = ParkingCalculatorPageObject(self.driver)
        pcpo.lot = 'EP'
        pcpo.start_time = '12:00'
        pcpo.start_date = '07/07/2015'
        pcpo.end_time = '12:00'
        pcpo.end_date = '07/17/2015'

        pcpo.calculate()

        pcpo.check_value()


if __name__ == "__main__":
    unittest.main()
