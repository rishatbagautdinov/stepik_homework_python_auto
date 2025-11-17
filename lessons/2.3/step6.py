from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'https://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
    
    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element(By.ID, 'input_value')
    x = x.text
    res = calc(x)

    inp = browser.find_element(By.ID, 'answer')
    inp.send_keys(res)

    button2 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button2.click()
    
    alert = browser.switch_to.alert
    alert_text = alert.text
    answer = alert_text.split(': ')[-1]
    print(answer)
finally:
    sleep(10)
    browser.quit()