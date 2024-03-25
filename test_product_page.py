import pytest
import time
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):  # регистрация тестового пользователя
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()  # открываем страницу
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email, password)  # регистрируем нового пользователя
        page.should_be_authorized_user()  # проверяем, что пользователь залогинен

    # тест отсутствия сообщения об успехе до добавления товара в корзину у зарегистрированного пользователя
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link, 0)
        page.open()  # открываем страницу
        page.should_not_be_success_message()  # проверяем отсутсвие сообщения об успехе

    # тест проверки добавления товара в корзину зарегестрированным пользователем
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        # инициализируем Page Object, передаем в конструктор класса ProductPage(страницы товара) экземпляр драйвера и url адрес
        page = ProductPage(browser, link)
        page.open()  # открываем страницу
        page.add_product_to_cart()  # проверяем наличие кнопки добавления в корзину и добавляем товар в корзину
        # page.solve_quiz_and_get_code()  # рассчитываем результат математического выражения для получения проверочного кода
        name = page.get_name()  # получаем имя товара и сохраняем в переменную
        price = page.get_price()  # получаем цену товара и сохраняем в переменную
        page.should_be_right_name(name)  # проверяем совпадение названия товара в корзине
        page.should_be_right_price(price)  # проверяем совпадение цены товара в корзине


# параметризация для запуска теста разных товаров акции, падающий тест отмечен как xfail
@pytest.mark.parametrize('promo_offer',
                         ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
# тест проверки добавления товара в корзину, соответствия названия и цены товара в корзине
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    # инициализируем Page Object, передаем в конструктор класса ProductPage(страницы товара) экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.add_product_to_cart()  # проверяем наличие кнопки добавления в корзину и добавляем товар в корзину
    page.solve_quiz_and_get_code()  # рассчитываем результат математического выражения для получения проверочного кода
    name = page.get_name()  # получаем имя товара и сохраняем в переменную
    price = page.get_price()  # получаем цену товара и сохраняем в переменную
    page.should_be_right_name(name)  # проверяем совпадение названия товара в корзине
    page.should_be_right_price(price)  # проверяем совпадение цены товара в корзине


@pytest.mark.xfail
# тест отсутствия сообщения об успехе после добавления товара в корзину
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    # инициализируем Page Object, передаем в конструктор класса ProductPage(страницы товара) экземпляр драйвера и url адрес
    page = ProductPage(browser, link, 0)
    page.open()  # открываем страницу
    page.add_product_to_cart()  # проверяем наличие кнопки добавления в корзину и добавляем товар в корзину
    page.should_not_be_success_message()  # проверяем отсутсвие сообщения об успехе


# тест отсутствия сообщения об успехе до добавления товара в корзину
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link, 0)
    page.open()  # открываем страницу
    page.should_not_be_success_message()  # проверяем отсутсвие сообщения об успехе


@pytest.mark.xfail
# тест, который проверяет, что сообщение об успехе исчезает после добавления товара в корзину
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link, 0)
    page.open()  # открываем страницу
    page.add_product_to_cart()  # проверяем наличие кнопки добавления в корзину и добавляем товар в корзину
    page.should_not_be_success_message_after_adding_product_to_basket()  # проверяем отсутсвие сообщения об успехе


def test_guest_should_see_login_link_on_product_page(browser):  # тест наличия ссылки на логин
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.should_be_login_link()  # проверяем наличие ссылки на логин


def test_guest_can_go_to_login_page_from_product_page(
        browser):  # тест перехода на страницу логина и проверка страницы логина
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.go_to_login_page()  # переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()  # вызываем метод проверки страницы логина


def test_guest_cant_see_product_in_basket_opened_from_product_page(
        browser):  # тест проверки корзины после перехода со страницы товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()  # открываем страницу товара
    page.go_to_basket_page()  # проверяем наличие ссылки на корзину и перехода на страницу корзины
    basket_page = BasketPage(browser, browser.current_url, 0)
    basket_page.should_be_empty_basket()  # проверяем отсутствие товаров в корзине
    basket_page.should_be_empty_basket_message()  # проверяем наличие сообщения о пустой корзине