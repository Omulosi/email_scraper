import re
from urllib import robotparser
from urllib.parse import urljoin
from lxml.html import fromstring

import requests
from constants import USER_AGENT

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_binary
import os


def get_driver():
    options = webdriver.ChromeOptions()
    # options.add_experimental_option("prefs", {
    #   "safebrowsing.enabled": True,
    # })
    options.add_argument("--disable-extensions")
    options.add_argument("--enable-javascript")
    options.add_argument("--headless")

    driver = webdriver.Chrome(chrome_options=options)

    # prevent bugs due to elements not loading properly in headless mode
    driver.set_window_size(1440, 900)
    return driver
