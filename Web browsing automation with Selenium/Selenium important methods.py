# Dummy code 

#Drag and Drop

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('')
source = driver.find_element_by_xpath('')
destination = driver.find_element_by_xpath('')
action = ActionChains(driver)
action.drag_and_drop(source,destination).perform()


#Wait Functions (Explicit and Inplicit)

# -> Explicit ( It Waits for some content to load)

#Libraries: 
webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

url='https://www.google.com/earth/'
driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
launch_earth_buttom=wait.until(EC.element_to_be_clickable((By.XPATH( ' enter XPath '))) )



 

