from lxml.html import fromstring
import requests
from urllib.parse import urljoin, urlparse
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from url_downloader import get_driver
from constants import DIRECTORIES  

def rutgers_scraper(name):
    print('Saving ' + name + "'s email...")
    query_link = DIRECTORIES.get('rutgers')
    driver = get_driver()
    driver.get(query_link)
    driver.implicitly_wait(15)
    time.sleep(5)
    driver.find_element_by_id('q').send_keys(
        name + Keys.RETURN)
    # pg_loaded = WebDriverWait(driver, 30).until(
    #     EC.presence_of_element_located((By.ClassName, "results")))
    time.sleep(5)
    driver.implicitly_wait(30)
    tree = fromstring(driver.page_source)
    email = tree.xpath('//div[contains(@id, "content")]//dd//a[contains(@href, "mailto")]/text()')
    print('===> ', email)
    driver.quit()
    return email[0] if email else 'NA'

