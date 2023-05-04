import os
from selenium import webdriver

os.environ['DISPLAY'] = ':10'  # Set the DISPLAY variable


# Set the path to the Chromium browser executable
chrome_path = '/usr/bin/google-chrome'

# Create a ChromiumOptions object to configure the browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')  
chrome_options.add_argument('--headless')  

chrome_options.binary_location = chrome_path
# chrome_options.add_argument('--headless')  # Run Chromium in headless mode

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(chrome_options=chrome_options)

# Navigate to a web page
driver.get('https://www.google.com')
print(driver.title)
input()
# Get the page title

# Close the browser
driver.quit()