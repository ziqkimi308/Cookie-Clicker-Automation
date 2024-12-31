"""
********************************************************************************
* Project Name:  Cookie Clicker Automation
* Description:   This project automates the popular browser-based game Cookie Clicker using Selenium. 
* Author:        ziqkimi308
* Created:       2024-12-31
* Updated:       2024-12-31
* Version:       1.0
********************************************************************************
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

# CONSTANT
CHROME_DRIVER_PATH = r""
WEBSITE_URL = "https://orteil.dashnet.org/experiments/cookie/"

# Setup driver
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.get(WEBSITE_URL)

cookie_click = driver.find_element(By.ID, "cookie")

# Continuous click and buy if money > price, buy the most expensive one
print("Time start now!")
# Condition for if statement inside loop
last_checked_time = time.time()
# Condition to break the loop must be outside of loop
time_end = time.time() + 60*5
while True:
	# Click
	cookie_click.click()

	# Check if it is already 5 seconds, then check if you can afford to upgrade
	if time.time() > last_checked_time:
		cookie_price_raw = driver.find_elements(By.CSS_SELECTOR, "#store > div:not(.grayed)")
		try:
			cookie_price_raw[-1].click()
		except:
			pass

		# Update the time last checked to current time
		last_checked_time = time.time() + 5

			# Check break condition
	if time.time() > time_end:
		cookies_per_second = driver.find_element(By.ID, "cps")
		print(cookies_per_second.text)
		break

# Last
driver.quit()
