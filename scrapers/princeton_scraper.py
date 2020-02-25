
from lxml.html import fromstring
import requests
from urllib.parse import urljoin, urlparse

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from url_downloader import download, get_driver

def princeton_scraper(name):
    print('Saving ' + name + "'s email...")
    query_link = DIRECTORIES.get('princeton')
    driver = get_driver()
    driver.get(query_link)
    driver.find_element_by_id('edit-search').send_keys(
        name + Keys.RETURN)
    # pg_loaded = WebDriverWait(driver, 30).until(
    #     EC.presence_of_element_located((By.ClassName, "results")))
    driver.implicitly_wait(5)
    driver.find_element_by_id('people-label').click()
    tree = fromstring(driver.page_source)
    email = tree.xpath('//div[contains(@class, "people-search-email")]/a/text()')
    driver.quit()
    return email[0] if email else 'NA'

