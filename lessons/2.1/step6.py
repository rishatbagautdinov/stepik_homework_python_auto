from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

people_radio = browser.find_element(By.ID, "peopleRule")
people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked == "true", "People radio is not selected by default"

robots_radio = browser.find_element(By.ID, "robotsRule")
robots_checked = robots_radio.get_attribute("checked")
print("value of robot radio: ", robots_checked)
assert robots_checked is None

# Попробовал что-то:
# button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
# button_checked = button.get_attribute('disabled')
# print('value of button status: ', button_checked)
# assert button_checked is None, 'Button is disabled by default'

# time.sleep(5)
# print('value of button status: ', button_checked)
# assert button_checked is not None, 'Button is not disabled by default'
