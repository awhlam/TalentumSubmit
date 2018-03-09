# Talentum Submit
# Version 1.0
# 03/09/18

# Import packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Setup web driver
chromedriver = "chromedriver.exe"
browser = webdriver.Chrome(executable_path=chromedriver)

# Load Talentum website
browser.get("https://apex.ftianalytics.com/ords/w_001000_0007/f?p=269:LOGIN::::::")

# Submit username/password to login
browser.find_element_by_id("P101_USERNAME").send_keys("YOURTALENTUMUSERNAME")
browser.find_element_by_id("P101_PASSWORD").send_keys("YOURTALENTUMPASSWORD")
browser.find_element_by_id("P101_LOGIN").click()

# Edit and Submit Forecast
browser.find_element_by_link_text("Edit Time Forecast").click()
browser.find_element_by_link_text("Submit Forecast").click()

# Close web driver
driver.quit()