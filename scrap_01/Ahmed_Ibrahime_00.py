import os 
os.chdir(r'c:\D')

from selenium import webdriver
import time as t 
from selenium.webdriver.common.keys import keys
from selenium.webdriver.common.by import By
import urllib
import cv2
import os

try:
    os.mkdir('dataset_download')
except:
    pass

name ='giraffe'

chrome_options = webdriver.ChromeOptions() 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

driver = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_options);  
url = ''
driver.get(url)
t.sleep(3)
pics = driver.find_element_by_xpath('')
links = []
x=1
last_height = 0
def download_image(url,filename):
    resource = urllib.request.urlopen(url)
    output = open(filename,'wb')
    output.write(resource.read())
    output.close()
while 1:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    t.sleep(4)
    pics_  = pics.find_elements_by_xpath('./*')
    for pic in pics_:
        try:
            img_link = pic.find_element_by_xpath('a[1]/div[1]/img').get_attribute('src')
            if img_link not in links:#check if link in list 
                links.append(img_link)
                try:
                    os.mkdir('dataset_download//'+name)
                except:
                    pass
                # try:
                #     os.mkdir('dataset_crop//'+name)
                # except:
                #     pass
                file_name ='dataset_download//'+name+'//'+str(x)+'.png'
                download_image(img_link,file_name)
                x +=1
        except:
            print('-',end='')
        
    new_height = driver.execute_script('return document.body.scrollHeight')
    print(new_height)
    if new_height == last_height:
        break
    last_height = new_height
    
driver.close()
