from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r'/Users/tess/Desktop/seleniumChrome/chromedriver')
driver.get("http://www.python.org")

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
time.sleep(8)

driver.close()
