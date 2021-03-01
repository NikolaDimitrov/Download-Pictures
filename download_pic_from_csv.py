import pandas as pd
import csv
import row as row
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
import urllib

PROXY = "5.157.14.191:12345"
url = 'https://reklama-varna.com/%D0%94%D0%B5%D0%BA%D0%BE%D1%80%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%BE-%D0%B8%D0%B7%D1%80%D1%8F%D0%B7%D0%B0%D0%BD%D0%B8-%D0%BB%D0%B0%D0%BC%D0%B0%D1%80%D0%B8%D0%BD%D0%B8-%D0%B7%D0%B0-%D0%BE%D0%B3%D1%80%D0%B0%D0%B4%D0%BD%D0%B8-%D0%BF%D0%B0%D0%BD%D0%B0-%D0%B8-%D0%B2%D1%80%D0%B0%D1%82%D0%B8-2?page=1'


options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=' + PROXY)
options.add_argument('headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)



with open('PIC.csv', encoding='utf8') as f:
    list_of_dict = [{k: v for k, v in row.items()}
    for row in csv.DictReader(f,skipinitialspace = True)]


count = 0
for i in list_of_dict:
    count += 1
    print(count)
    name = i['Name']
    driver.get(i['URL Product'])
    time.sleep(3)
    pic = driver.find_element_by_class_name('product-page-content').find_element_by_class_name(
        'image').find_element_by_tag_name('a').get_attribute('href')
    urllib.request.urlretrieve(pic, f"C:/Users/Nikola/Desktop/Pic/{name}")
    # time.sleep(3)
