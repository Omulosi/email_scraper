from lxml.html import fromstring
import requests
from urllib.parse import urljoin, urlparse
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium

from url_downloader import download, get_driver
from constants import DIRECTORIES 

def stony_brook_scraper(name):
    print('Saving ' + name + "'s email...")
    query_link = DIRECTORIES.get('stony brook')
    driver = get_driver()
    driver.get(query_link)
    driver.implicitly_wait(15)
    time.sleep(5)
    driver.find_element_by_css_selector('.site-input > input').send_keys(
        name + Keys.RETURN)
    # pg_loaded = WebDriverWait(driver, 30).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, "data")))
    #time.sleep(30)
    driver.implicitly_wait(30)
    try:
    	driver.find_element_by_xpath('//tr[@class="data"]//a[@class="email"]/text()')
    except selenium.common.exceptions.NoSuchElementException:
    	driver.execute_script("location.reload()")
    	driver.find_element_by_css_selector('.site-input > input').send_keys(
        name + Keys.RETURN)
    # tree = fromstring(driver.find_element_by_tag_name('body').get_attribute('innerHTML'))
    time.sleep(5)
    tree = fromstring(driver.page_source)
    email = tree.xpath('//tr[@class="data"]//a[@class="email"]/text()')
    import pdb
    pdb.set_trace()
    print(email)
    time.sleep(2)
    driver.quit()
    return email[0] if email else 'NA'