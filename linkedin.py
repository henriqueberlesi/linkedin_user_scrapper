from selenium import webdriver
from linkedin_functions import *
from selenium.common.exceptions import NoSuchElementException
import json

driver = webdriver.Firefox()

login(driver, 'blabla@blabla.com', '123456')

# dado uma lista

users = ['HENRIQUE BERLESI']

for user in users:
    u = Search(user, driver)
    u.save('results.csv')