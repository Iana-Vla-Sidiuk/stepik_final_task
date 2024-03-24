from selenium.webdriver.common.by import By

class MainPageLocators(): #создание класса MainPageLocators (локаторы главной страницы)
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  #переменная для селектора ссылки на логин
    
class LoginPageLocators(): #создание класса LoginPageLocators (локаторы страницы логина)
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")  #переменная для селектора формы регистрации
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")  #переменная для селектора формы логина

class ProductPageLocators(): #создание класса ProductPageLocators (локаторы страницы товара)
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")  #переменная для селектора кнопки добавления в корзину
    NAME = (By.CSS_SELECTOR, ".col-sm-6 h1")  #переменная для селектора названия товара
    PRICE = (By.CSS_SELECTOR, ".col-sm-6 .price_color")  #переменная для селектора цены товара
    BOOK_NAME = (By.CSS_SELECTOR, ".alert:first-child strong")  # переменная для селектора названия товара в корзине
    BOOK_PRICE = (By.CSS_SELECTOR, ".alert:last-child strong")  # переменная для селектора цены товара в корзине