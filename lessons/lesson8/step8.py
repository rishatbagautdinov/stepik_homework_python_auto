from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

try:
    link = 'https://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    f_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    f_name.send_keys('Rishat')

    l_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    l_name.send_keys('Bagautdinov')

    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    email.send_keys('labuba@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    file = browser.find_element(By.ID, 'file')
    file.send_keys(file_path)

    btn = browser.find_element(By.XPATH, '//button[@type="submit"]')
    btn.click()
finally:
    sleep(5)
    browser.quit()