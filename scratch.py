import os
from selenium import webdriver

# os.environ['DISPLAY'] = ':10'  # Set the DISPLAY variable


# Set the path to the Chromium browser executable
# chrome_path = '/usr/bin/google-chrome'

# Create a ChromiumOptions object to configure the browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')  
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--window-position=0,0')
chrome_options.add_argument('--start-maximized')

# chrome_options.add_argument('--headless')  

# chrome_options.binary_location = chrome_path
# chrome_options.add_argument('--headless')  # Run Chromium in headless mode

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(chrome_options=chrome_options)

# Navigate to a web page
driver.get('https://www.google.com')
print(driver.title)
driver.get_screenshot_as_file('screenshot.png')
input()
# Get the page title

# Close the browser
driver.quit()