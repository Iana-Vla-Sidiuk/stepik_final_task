import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, browser):  # тест наличия ссылки на логин
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()  # открываем страницу
        page.should_be_login_link()  # проверяем наличие ссылки на логин

    def test_guest_can_go_to_login_page(self, browser):  # тест перехода на страницу логина и проверка страницы логина
        link = "http://selenium1py.pythonanywhere.com/"
        # инициализируем Page Object, передаем в конструктор класса MainPage(главной страницы) экземпляр драйвера и url адрес
        page = MainPage(browser, link)
        page.open()  # открываем страницу
        page.go_to_login_page()  # переходим на страницу логина
        # инициализируем Page Object, передаем в конструктор класса LoginPage(страницы логина) экземпляр драйвера и текцщий url адрес
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()  # вызываем метод проверки страницы логина

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser): #тест проверки корзины после перехода с главной страницы
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()                                  # открываем главную страницу
    page.go_to_basket_page()                     # проверяем наличие ссылки на корзину и перехода на страницу корзины
    basket_page = BasketPage(browser, browser.current_url, 0)
    basket_page.should_be_empty_basket()         # проверяем отсутствие товаров в корзине
    basket_page.should_be_empty_basket_message() # проверяем наличие сообщения о пустой корзине