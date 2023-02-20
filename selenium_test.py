import numpy
from selenium import webdriver
# from seleniumwire import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from webdriver_manager.chrome import ChromeDriverManager

WAIT = 20
URL  = 'https://www.toyotacf.com/ccpa-policy/'

def setDriver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("disable-popup-blocking")
    chrome_options.add_argument("disable-notifications")
    chrome_options.add_argument("disable-popup-blocking")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_options)
  
    # sleep = 100000
    return driver
def main():

	driver = setDriver()
	print('Set Driver')
	driver.get(URL)
	html = driver.page_source
	with open("1.html", "w", encoding="utf-8") as f:
		f.write(html)
		f.close()
	print('Get to the Link')
	print(html)
	#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, selector['header'])))
main()