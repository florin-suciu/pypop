# from selenium import webdriver

DRIVER = None
LOG_PATH = "/home/florin/logs/pypop/main.log"


def setDriver(driver):
    global DRIVER
    DRIVER = driver
