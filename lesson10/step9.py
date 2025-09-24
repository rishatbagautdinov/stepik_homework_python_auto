from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from calc import Calc

browser = webdriver.Chrome()

link = browser.get("https://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
text = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
button = browser.find_element(By.ID, 'book')
button.click()

x = browser.find_element(By.ID, 'input_value')
x = x.text
res = Calc.calc(x)

inp = browser.find_element(By.ID, 'answer')
inp.send_keys(res)

button2 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
button2.click()

alert = browser.switch_to.alert
alert_text = alert.text
answer = alert_text.split(': ')[-1]
print(answer)