import time
from lxml.html import fromstring
import requests
from urllib.parse import urljoin, urlparse

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium

from url_downloader import get_driver
from utils import DIRECTORIES
from cache import Cache

def michigan_scraper(name):
    print('Retrieving ' + name + "'s email...")
    cache = Cache()
    try:
        email = cache[name]
        return email
    except KeyError:
        pass
    name = name.replace(" ", "%20")
    query_link = DIRECTORIES.get('michigan')
    query_link = query_link.format(name)
    driver = get_driver()
    driver.get(query_link)
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_xpath('//div[@id="peopleContent"]//table[@class="searchResults"]//tbody//tr[1]//td[1]//a[1]').click()
        driver.implicitly_wait(20)
        email = driver.find_element_by_xpath('//div[contains(@class, "wrapEmail")]//a[contains(@href, "mailto")]')
        email = email.text
        print(email)
    except selenium.common.exceptions.NoSuchElementException:
        email = None
    driver.quit()
    if email is not None:
        cache[name] = email
    return email

