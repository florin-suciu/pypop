from pageobjects.seleniumwrapper import SeleniumWrapper

from selenium.webdriver.common.by import By


selenium_server_connection = SeleniumWrapper()

#==================================================================================================
# parking calculator page locators
#==================================================================================================
locators = {}
locators['parking.lot'] = 'Lot', By.ID
locators['parking.entry_time'] = 'EntryTime', By.ID
locators['parking.entry_date'] = 'EntryDate', By.ID
locators['parking.exit_time'] = 'ExitTime', By.ID
locators['parking.exit_date'] = 'ExitDate', By.ID
locators['parking.calculate'] = '//input[@type="submit" and @name="Submit"]', By.XPATH
# TODO: following 2 locators are not good, need updating
locators['parking.result_price'] = 'SubHead', By.CLASS_NAME
locators['parking.result_time'] = 'BodyCopy', By.CLASS_NAME
