from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "img[id='treasure']")
    valuex = x_element.get_attribute('valuex')
    y = calc(valuex)
    inp = browser.find_element(By.CSS_SELECTOR, '#answer')
    inp.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    checkbox.click()
    radio = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
finally:
    time.sleep(10)
    browser.quit()