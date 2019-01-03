from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

if __name__ == "__main__":
    # Setup web driver
    chromedriver = "chromedriver.exe"
    options = Options()
    options.binary_location = 'C:\\Program Files (x86)\\Google\\Chrome Beta\\Application\\chrome.exe'
    browser = webdriver.Chrome(chromedriver, chrome_options=options)

    # Load Talentum website
    browser.get("https://apex.ftianalytics.com/ords/w_001000_0007/f?p=269:LOGIN::::::")

    # Submit username/password to login
    browser.find_element_by_id("P101_USERNAME").send_keys("USERNAME")
    browser.find_element_by_id("P101_PASSWORD").send_keys("PASSWORD")
    browser.find_element_by_id("P101_LOGIN").click()

    # Edit and Submit Forecast
    browser.find_element_by_link_text("Edit Time Forecast").click()
    browser.find_element_by_link_text("Submit Forecast").click()

    # Close web driver
    browser.quit()
