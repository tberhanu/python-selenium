from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'/Users/tess/Desktop/seleniumChrome/chromedriver')

driver.implicitly_wait(10)

driver.get('http://www.python.org')
myDynamicElement = driver.find_element_by_id('start-shell')

driver.close()
