from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_should_see_login_link(browser): # тест наличия ссылки на логин
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()                     # открываем страницу
    page.should_be_login_link()     # проверяем наличие ссылки на логин

def test_guest_can_go_to_login_page(browser): #тест перехода на страницу логина и проверка страницы логина
    link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем в конструктор класса MainPage(главной страницы) экземпляр драйвера и url адрес
    page = MainPage(browser, link)   
    page.open()                      # открываем страницу
    page.go_to_login_page()          # вызываем метод перехода на страницу логина 
    # инициализируем Page Object, передаем в конструктор класса LoginPage(страницы логина) экземпляр драйвера и текцщий url адрес
    login_page = LoginPage(browser, browser.current_url) 
    login_page.should_be_login_page() # вызываем метод проверки страницы логина

    
