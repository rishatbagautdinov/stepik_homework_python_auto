from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'https://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = int(x.text)
    y = calc(x)

    inpu = browser.find_element(By.ID, 'answer')
    inpu.send_keys(y)
    
    checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    checkbox.click()
    
    browser.execute_script('window.scrollBy(0, 100);')
    
    radio = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radio.click()
    
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
finally:
    sleep(5)
    browser.quit()
