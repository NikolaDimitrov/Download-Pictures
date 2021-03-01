from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import urllib


profile_url = []


def main_settings():
    proxy = "5.157.14.191:12345"
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=' + proxy)
    options.add_argument('headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    for i in range(1, 37):
        print(i)
        num = str(i)
        settings_driver(num, driver)

    make_csv_file()


def settings_driver(num, driver):
    driver.get(f'https://reklama-varna.com/%D0%94%D0%B5%D0%BA%D0%BE%D1%80%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%BE-%D0%B8%D0%B7%D1%80%D1%8F%D0%B7%D0%B0%D0%BD%D0%B8-%D0%BB%D0%B0%D0%BC%D0%B0%D1%80%D0%B8%D0%BD%D0%B8-%D0%B7%D0%B0-%D0%BE%D0%B3%D1%80%D0%B0%D0%B4%D0%BD%D0%B8-%D0%BF%D0%B0%D0%BD%D0%B0-%D0%B8-%D0%B2%D1%80%D0%B0%D1%82%D0%B8-2?page={num}')
    time.sleep(3)
    scrap_data(driver, num)


def scrap_data(driver, num):
    plot = driver.find_element_by_class_name('main-products')
    url_prod = plot.find_elements_by_class_name('name')
    count = 0
    for item in url_prod:
        count += 1
        table = {}
        name = f'page{num}-product{count}.jpg'
        url_product = item.find_element_by_tag_name('a').get_attribute('href')
        table['Name'] = name
        table['Page URL'] = driver.current_url
        table['URL Product'] = url_product


        profile_url.append(table)



def make_csv_file():
    df = pd.DataFrame(profile_url)
    df.to_csv('PIC.csv', encoding='utf-8-sig', index=False)


main_settings()
