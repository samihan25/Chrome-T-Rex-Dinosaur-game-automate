from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#creating object of Firefox driver
browser = webdriver.Firefox()

#open website which have chrome T-Rex dino game
browser.get('https://chromedino.com/')
time.sleep(1)

#select some element
elem = browser.find_element_by_id('t')

#outer loop for every new game
while True:
    #inner loop for each step in a game
    while True:
        elem.send_keys(Keys.SPACE)
        time.sleep(0.3)             # Time gap of 30 miliseconds is given between each move
    time.sleep(1)                   # Time gap of 1 second between each different game
