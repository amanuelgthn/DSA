#!/usr/bin/env python3

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# The URL of the page you want to monitor
url = "https://pobyt-czasowy-zapis-na-zlozenie-wniosku.mazowieckie.pl/"

# Setting up the Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # This option keeps the Chrome window open
driver = webdriver.Chrome(options=options)
driver.get(url)

# Function to check for specific content
def check_for_content(driver, text):
    try:
        # Modify the XPath to the correct path where the text might appear
        # This is just an example looking for any element containing the text
        driver.find_element_by_xpath(f"//*[contains(text(), '{text}')]")
        return True
    except NoSuchElementException:
        return False

# Specific text to look for
specific_text = """
The receipt of applications for submitting an application for temporary residence in the session of April 22, 2024 has ended. We encourage you to register via the application form at the next date. The date of activation of the next session of the application form will be available on the website migrant.wsc.mazowieckie.pl .
What happened?
The proxy failed to connect to the web server, due to TCP connection timeout.
Your IP: 194.29.137.21
Proxy IP: 45.60.74.103 (ID 10688-100)
Incident ID: 688000020041244887-73148812128944263
Connection Failed
Error 20
temporary-stay-registration-for-submission-wniosku.mazowieckie.pl
2024-04-29 04:51:56 UTC"""

# Check every 30 seconds
while True:
    time.sleep(30)  # Wait for 30 seconds before refreshing the page
    if check_for_content(driver, specific_text):
        print(f"Text '{specific_text}' found, stopping refresh.")
        break
    else:
        print(f"Text '{specific_text}' not found, refreshing page.")
        driver.refresh()

# The script now does not include `driver.quit()` to avoid closing the browser.
