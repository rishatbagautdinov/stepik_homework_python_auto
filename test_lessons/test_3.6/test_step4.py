from selenium.webdriver.common.by import By
import time

def test_auth(browser, credentials):
    login, password = credentials
    link = 'https://stepik.org/lesson/236895/step/1'
    browser.implicitly_wait(5)
    browser.get(link)
    sign_in = browser.find_element(By.XPATH, '//a[@class="ember-view navbar__auth navbar__auth_login st-link st-link_style_button"]')
    sign_in.click()
    login_inp = browser.find_element(By.XPATH, '//input[@name="login"]')
    login_inp.send_keys(login)
    password_inp = browser.find_element(By.XPATH, '//input[@name="password"]')
    password_inp.send_keys(password)
    btn = browser.find_element(By.XPATH, '//button[@class="sign-form__btn button_with-loader "]')
    btn.click()