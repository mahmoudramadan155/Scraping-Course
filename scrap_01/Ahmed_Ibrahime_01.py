import os 
os.chdir(r'c:\D')

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time as t 
from selenium.webdriver.common.keys import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib
import cv2
import os
import wget

try:
    os.mkdir('dataset_download')
except:
    pass

name ='giraffe'

# chrome_options = webdriver.ChromeOptions() 
# chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
# driver = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_options);  
driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://elzero.org'
driver.get(url)

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']")))


username.clear()
username.send_keys('username')
password.clear()
password.send_keys('password')

button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[type='submit']"))).click()

not_now = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,"//button[contain(text(),'Not Now')]"))).click()
not_now2 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,"//button[contain(text(),'Not Now')]"))).click()

searchbox = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,"//input[@palceholder='search']")))
searchbox.clear()

keyword = '#cat'
searchbox.send_keys(keyword)

t.sleep(1)
searchbox.send_keys(keys.ENTER)
t.sleep(1)
searchbox.send_keys(keys.ENTER)
t.sleep(1)

driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
t.sleep(2)

images = driver.find_element_by_tag_name('img')
image = [image.get_attribute('src') for image in images]
print(images)
print(len(images))

path = os.getcwd()
path = os.path.join(path,keyword[1:]+'s')
os.mkdir(path)

counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:]+str(counter)+'.jpg')
    wget.download_image(image,save_as)
    counter +=1
