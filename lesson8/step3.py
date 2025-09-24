from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element(By.ID, 'num1')
    num1 = int(num1.text)
    print('Type of num1: ', type(num1), ' Value of num2: ' , num1)
    num2 = browser.find_element(By.ID, 'num2')
    num2 = int(num2.text)
    print('Type of num2: ', type(num2), ' Value of num2: ' , num2)
    sum = num1 + num2
    print('sum is ', sum)
    print(type(sum))
    select = Select(browser.find_element(By.ID, 'dropdown'))
    print('select is ', select)
    str_sum = str(sum)
    print('type of str_sum is ', type(str_sum))
    select.select_by_visible_text(str_sum)
    
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
finally:
    time.sleep(5)
    browser.quit()