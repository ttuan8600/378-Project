import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox() #ask Faizan if this would work with the connection to the server?
driver.get("google.com")
input()
#run the information got from website data?
# email_field = driver.find_element_by_name('email')
# password_field = driver.find_element_by_name('password')
# email_field.send_keys('# the email')
# password_field.send_keys('the password')
# password_field.send_keys(Keys.RETURN)

time.sleep(5)

# subprocess.run(['python3', 'runmain.py', '-emailuser@example.com', '-passwordpassword'])

driver.quit()