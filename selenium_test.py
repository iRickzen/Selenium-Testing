import time
from selenium import webdriver

driver_path = './chromedriver.exe'
driver = webdriver.Chrome(driver_path)

#Open website "google"
driver.get('http://www.google.com/xhtml');
time.sleep(5)
search_box = driver.find_element_by_name('q')
search_box.send_keys('Do a barrel roll')
time.sleep(2) #some delay to see input
search_box.submit()

#some_element = driver.find_element_by_xpath('//*[@id="taw"]/div[2]/div[1]/p/a')
#some_element.click()


time.sleep(5)
driver.quit()

