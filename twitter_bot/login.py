from selenium import webdriver
import time
import os

from dotenv import load_dotenv  # for python-dotenv method
load_dotenv()

web = "https://twitter.com/i/flow/login"
path = os.environ.get("DRIVER_PATH")
driver = webdriver.Chrome(path)
driver.get(web)

time.sleep(6)

username = driver.find_element_by_xpath('//input[@autocomplete="username"]')
username.send_keys(os.environ.get('USER'))

next_button = driver.find_element_by_xpath(
    '//div[@role="button"]//span[text()="Next"]')
next_button.click()


time.sleep(2)

password = driver.find_element_by_xpath(
    '//input[@autocomplete="current-password"]')
password.send_keys(os.environ.get('PASSWORD'))

login_button = driver.find_element_by_xpath(
    '//div[@role="button"]//span[text()="Log in"]')
login_button.click()
