from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time as t 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib
import cv2
import os
import wget

print(os.chdir(r'D:\Games\UpWork\Scraping'))
print(os.getcwd())

driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://elzero.org'
driver.get(url)
driver.find_element_by_css_selector("input[name='s']").send_keys('Front-End Developer')
driver.find_element_by_css_selector('.search-submit').click()
driver.implicitly_wait(5)
driver.find_element_by_css_selector('.all-search-posts .search-post:first-of-type h3 a').click()
driver.implicitly_wait(5)
veiw_c = driver.find_element_by_css_selector('.z-article-info .z-info:last-of-type span:last-child')
print(veiw_c.get_attribute('innerHTML'))
driver.quit()