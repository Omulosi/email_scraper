mport requests,re
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
options = Options()
options.add_argument('-headless')
import pandas as pd
from bs4 import BeautifulSoup


def penn_scraper(name, institution):
	browser = webdriver.Firefox(options=options)
	titles = ['Dr.', 'Mr.','Prof.','Ms.']
	for title in titles:
		if title in name:
			name.replace(title, '')
	fname, lname = name.split(maxsplit=2)	
	print(fname,lname)
	browser.get("https://medley.isc-seo.upenn.edu/directory/jsp/fast.do")
	sleep(2)
	browser.find_element_by_name("lastName").clear()
	browser.find_element_by_name("lastName").send_keys(lname)
	allfields = browser.find_elements_by_class_name("fastFormField")
	allfields[1].clear()
	allfields[1].send_keys(fname)

	sleep(1)
	browser.find_element_by_class_name("fastButtonLinkText").click()
	

	soup = BeautifulSoup(browser.page_source, "lxml")
	
	email = soup.find(href=re.compile("@"))
	if email is None:
		email = 'NA'
	else:
		email = email.string
	print('Email :',email)		
	browser.quit()
	return email