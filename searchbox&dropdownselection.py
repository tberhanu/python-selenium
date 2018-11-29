from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path=r'/Users/tess/Desktop/seleniumChrome/chromedriver')
driver.get("https://wiki.python.org/moin/FontPage")

searchBox = driver.find_element_by_id("searchinput")
searchBox.clear()
searchBox.send_keys('Beginner')
searchBox.send_keys(Keys.ENTER)
time.sleep(5)

driver.get("https://wiki.python.org/moin/BeginnerErrorsWithPythonProgramming")
select= Select(driver.find_element_by_xpath("//*[@id='sidebar']/div[3]/ul/li[5]/form/div/select"))
select.select_by_visible_text("Raw Text")

time.sleep(5)

driver.close()
