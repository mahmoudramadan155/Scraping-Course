from selenium import webdriver
import csv
from webdriver_manager.chrome import  ChromeDriverManager
import os

print(os.chdir(r'D:\Games\UpWork\Scraping'))
print(os.getcwd())

# opening a webpage with options
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

# opening a webpage




driver.get('https://www.sos.ca.gov/state-holidays')
date = driver.find_elements_by_xpath('//table[@summary="Dates of observed state holidays in 2020."]//td[1]')
holidays = driver.find_elements_by_xpath('//table[@summary="Dates of observed state holidays in 2020."]//td[2]')

with open('holidays.csv', 'w' , newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['date','holidays'])
    for i in range(1,len(date)):
        csvwriter.writerow([date[i].text,holidays[i].text])



# for dates in date:
#     print(dates.text)


# for holiday in holidays:
#     print(holiday.text)
    
# closing the current window
# driver.close()