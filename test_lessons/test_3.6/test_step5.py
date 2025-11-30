import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize('link', [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
])
def test_auth(browser, credentials, link):
    login, password = credentials

    print(f"\nОткрываем: {link}")
    browser.get(link)

    print("Кликаем логин")
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login"))
    ).click()

    print("Заполняем форму")
    browser.find_element(By.NAME, "login").send_keys(login)
    browser.find_element(By.NAME, "password").send_keys(password)
    browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()

    print("Ждём поле ввода")
    answer_area = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.string-quiz__textarea"))
    )

    print("Вводим ответ")
    answer = str(math.log(int(time.time())))
    answer_area.send_keys(answer)

    print("Жмём Отправить через JS")
    browser.execute_script("setTimeout(() => document.querySelector('button.submit-submission')?.click(), 600);")

    print("Ждём появления 'Correct!'")
    feedback = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint"))
    )
    print(f'Получили - "{feedback.text}"')

    # Вот и всё! Только assert — как ты и хотел
    assert feedback.text == "Correct!", f"Ожидали 'Correct!', а получили: '{feedback.text}'"