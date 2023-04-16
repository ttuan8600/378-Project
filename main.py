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


class startChrome:
#args used to bypass bot check
    
    # #open the page

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element("xpath",xpath)
        except NoSuchElementException:
            return False
        return True
    def restart(self):
        print("restarting now")
        self.driver.close()
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument('--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"')

        self.chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(chrome_options=self.chrome_options, executable_path='/snap/bin/chromium.chromedriver')
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.driver.get('https://sso.csulb.edu/')

    def __init__(self):
        # self.url = 'https://sso.csulb.edu/'
        self.email = None
        self.password = None
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument('--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"')

        self.chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(chrome_options=self.chrome_options, executable_path='/snap/bin/chromium.chromedriver')
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    # email = input()
    # password=input()

        self.driver.get('https://sso.csulb.edu/')
    # time.sleep(6)

    def login_email(self, email,password):
        # print("login email")
        # return True
        print("login email: email :" + email)
        # print("login email: password :" + password )
        self.email = email
        self.password = password
        time.sleep(2)
        while not self.check_exists_by_xpath("//input[@type='submit']"):
            print("slep")
            time.sleep(4)
        self.driver.find_element("xpath","//input[@type='email']").send_keys(email)
        self.driver.find_element("xpath","//input[@type='submit']").click()
        time.sleep(2)
        self.driver.find_element("xpath","//input[@type='password']").send_keys(password)
        self.driver.find_element("xpath","//input[@type='submit']").click()
        time.sleep(3)
        if self.check_exists_by_xpath("//div[@id='passwordError']"):
            return False
        else:
            return True

    def call(self):
        time.sleep(2)
        self.driver.find_element("xpath","//div[@data-value='TwoWayVoiceMobile']").click()

    def text(self,email):
        time.sleep(2)
        while not self.check_exists_by_xpath("//input[@type='submit']"):
            time.sleep(2)
        self.driver.find_element("xpath","//div[@data-value='OneWaySMS']").click()
        code = self.get_code(email)
        self.driver.find_element("xpath","//input[@placeholder='Code']").send_keys(code)
        self.driver.find_element("xpath","//input[@type='submit']").click()
        time.sleep(5)

    def get_code(self, email):
        while not os.path.exists(email+".txt"):
            time.sleep(2)
        with open(email+".txt") as file:
            return file.readline().strip()

    def open_mycsulb(self):
        time.sleep(2)
        itter = 0
        while not self.check_exists_by_xpath("//button[@aria-label='MyCSULB Student Center app context menu']"):
            time.sleep(2)
            itter+=1
            if itter==10:
                return self.restart()
        btn = self.driver.find_element("xpath","//img[@src='https://secure.aadcdn.microsoftonline-p.com/dbd5a2dd-2zw3qm4qynz9c5fstygwvkdcrgzrj-6a-oirg1jenxo/appbranding/ekmndmb3vnaodjtwlqu-spdi39yp1wu-ixrh710b4nu/1033/bannerlogo?ts=637570610815243802']").click()

        
    def log_info(self):
        print("log_info check")
        time.sleep(2)
        print("title 1:" + self.driver.title)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        print("title 2:", self.driver.title)
        itter = 0
        while not self.check_exists_by_xpath("//span[@id='DERIVED_SSS_SCL_SSS_LONGCHAR_1']"):
            print("log_info self.check_exists_by_xpath")
            time.sleep(2)
            itter+=1
            if itter==10:
                return self.restart()
        # add1 = driver.find_element_by_xpath("//span[@id='DERIVED_SSS_SCL_SSS_LONGCHAR_1']").text
        # add2= driver.find_element_by_xpath("//span[@id='DERIVED_SSS_SCL_SSS_LONGCHAR_2']").text
        phone = self.driver.find_element("xpath","//span[@id='DERIVED_SSS_SCL_DESCR50']").text
        print("log_info phone")
        # prefemail= driver.find_element_by_xpath("//span[@id='DERIVED_SSS_SCL_EMAIL_ADDR']").text
        with open("data.txt", "a") as a:
            # line = add1+" | " + add2+" | "+phone+" | "+prefemail+" | "+email+" | "+" \n
            #  "
            print("log_info write")
            line = phone+" | "+self.email+" | "+" \n "
            a.write(line)
        print("log_info done")
        self.restart()


