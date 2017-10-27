import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import docker


### For debugging purpose use Real vnc and connect on localhost:5900
### check if container allready exists - only one standalone at a time is possible
docker_img = "selenium/standalone-chrome-debug:3.6.0-copper"
client = docker.from_env()
container = client.containers.list(filters={"ancestor":docker_img})

if container:  container = container[0]
else:
    container = client.containers.run(docker_img, detach=True, ports={'4444':'4444','5900':'5900'})

retries = 5 #try max 5 seconds in case container needs some time to start
while retries >= 0 and container.status != 'running':
    retries -= 1
    time.sleep(1)
### Selenium webdriver in docker-container ready to go


# get Selenium remote driver
driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)


driver.get('http://www.google.com/xhtml');
time.sleep(2) # delay to watch screen
search_box = driver.find_element_by_name('q')

search_box.send_keys('10+46')
time.sleep(1) # delay to watch screen
search_box.submit()
time.sleep(1) # delay to watch screen

calc_box = driver.find_element_by_id('cwos')

### finally some real testing
#print(calc_box.get_attribute("innerHTML"))
assert int(calc_box.get_attribute("innerHTML")) == 56


driver.quit()
# stop container
container.stop()


