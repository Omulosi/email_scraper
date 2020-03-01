import time
from lxml.html import fromstring
import requests
from urllib.parse import urljoin, urlparse

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from url_downloader import get_driver
from utils import DIRECTORIES
from cache import Cache

def princeton_scraper(name):
    print('Retrieving ' + name + "'s email...")
    cache = Cache()
    try:
        email = cache[name]
        return email
    except KeyError:
        pass
    query_link = DIRECTORIES.get('princeton')
    driver = get_driver()
    driver.get(query_link)
    driver.implicitly_wait(15)
    time.sleep(2)
    driver.find_element_by_id('edit-search').send_keys(
        name + Keys.RETURN)
    # pg_loaded = WebDriverWait(driver, 30).until(
    #     EC.presence_of_element_located((By.ClassName, "results")))
    time.sleep(3)
    driver.implicitly_wait(30)
    driver.find_element_by_id('people-label').click()
    tree = fromstring(driver.page_source)
    email = tree.xpath('//div[contains(@class, "people-search-email")]/a/text()')
    driver.quit()
    email = email[0] if email else None
    if email is not None:
        cache[name] = email
    return email

