import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import docker


#client = docker.from_env()
#container = client.containers.run("selenium/standalone-chrome:3.6.0-copper", detach=True, network="4444:4444")
#print(container)
#container = client.containers.get(container_id)



driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)


driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()



#container.stop()


