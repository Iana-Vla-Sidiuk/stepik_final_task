import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser): #обработчик, который считывает из командной строки параметр language
    parser.addoption('--language', action='store', default='en',
                 help="Choose language: '--language=en' or '--language=ru'")

@pytest.fixture(scope="function")
def browser(request):  #запуск браузера с указанным языком пользователя
    print("\nstart browser for test..")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()





