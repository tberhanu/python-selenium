from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path=r'/Users/tess/Desktop/seleniumChrome/chromedriver')
driver.get("file:///Users/tess/Desktop/seleniumChrome/html_code_03_02.html")
select= Select(driver.find_element_by_name("numReturnSelect"))
select.select_by_index(5)
time.sleep(2)
select.select_by_visible_text("200")
time.sleep(2)
select.select_by_value("250")
time.sleep(2)

drop_down_options = select.options
print(drop_down_options)

submit_button = driver.find_element_by_name("continue")
submit_button.submit()
time.sleep(2)

driver.close()
