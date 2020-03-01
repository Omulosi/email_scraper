from lxml.html import fromstring
import requests
from urllib.parse import urljoin, urlparse
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from url_downloader import get_driver
from utils import DIRECTORIES
from cache import Cache

def oak_ridge_scraper(name):
    print('Retrieving ' + name + "'s email...")
    query_link = DIRECTORIES.get('oak ridge')
    name = name.replace(" ", "+")
    cache = Cache()
    try:
        email = cache[name]
        return email
    except KeyError:
        pass
    query_link = query_link.format(name)
    driver = get_driver()
    driver.get(query_link)
    driver.implicitly_wait(20)
    driver.find_element_by_css_selector('td.views-field-nothing a:nth-child(1)').click()
    driver.implicitly_wait(10)
    try:
        email = driver.find_element_by_xpath('//div[contains(@class, "staff-profile-contact-info")]//a[contains(@href, "mailto")]')
        email = email.text
        print(email)
    except NoSuchElementException:
        email = None
    driver.quit()
    if email is not None:
        cache[name] = email
    return email
