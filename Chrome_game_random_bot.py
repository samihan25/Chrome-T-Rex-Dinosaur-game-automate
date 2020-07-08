from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from decouple import config
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Firefox()

browser.get('https://chromedino.com/')
time.sleep(1)
#assert 'Google' in browser.title
# time.sleep(2)
elem = browser.find_element_by_id('t')
while True:
    while True:
        elem.send_keys(Keys.SPACE)
        time.sleep(0.3)
    time.sleep(1)
