import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions  # ← исправили импорт
from selenium.webdriver.firefox.options import Options as FirefoxOptions  # ← исправили импорт
import os

# === Добавляем новый параметр --language ===
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None, help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en', help="Язык интерфейса браузера: ru, en, de, fr, es и т.д.")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")        # ← берём язык из командной строки

    # Переменная user_language больше не нужна — используем language
    if browser_name == "chrome":
        chrome_options = ChromeOptions()                   # ← правильный класс
        chrome_options.add_argument(f"--lang={language}")  # ← самый надёжный способ для Chrome
        # Дополнительно (на всякий случай)
        chrome_options.add_experimental_option(
            "prefs", {"intl.accept_languages": language}
        )
        print(f"\nstart chrome browser for test.. language: {language}")
        browser = webdriver.Chrome(options=chrome_options)

    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()                 # ← правильный класс
        firefox_options.set_preference("intl.accept_languages", language)
        print(f"\nstart firefox browser for test.. language: {language}")
        browser = webdriver.Firefox(options=firefox_options)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="session")
def credentials():
    config_path = "config.txt"
   
    if not os.path.exists(config_path):
        pytest.fail(f"Файл {config_path} не найден! Создай его и положи логин и пароль построчно.")
   
    with open(config_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]  # пропускаем пустые строки
   
    if len(lines) < 2:
        pytest.fail("В config.txt должно быть минимум 2 строки: логин и пароль")
   
    login = lines[0]
    password = lines[1]
   
    return login, password