from selenium.webdriver.common.by import By

class MainPageLocators(): #создание класса MainPageLocators (локаторы главной страницы)
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  #константа для селектора ссылки на логин
    
class LoginPageLocators(): #создание класса LoginPageLocators (локаторы страницы логина)
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")  #константа для селектора формы регистрации
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")  #константа для селектора формы логина

class ProductPageLocators(): #создание класса ProductPageLocators (локаторы страницы товара)
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")  #константа для селектора кнопки добавления в корзину
    NAME = (By.CSS_SELECTOR, ".col-sm-6 h1")  #константа для селектора названия товара
    PRICE = (By.CSS_SELECTOR, ".col-sm-6 .price_color")  #константа для селектора цены товара
    BOOK_NAME = (By.CSS_SELECTOR, ".alert:first-child strong")  #константа для селектора названия товара в корзине
    BOOK_PRICE = (By.CSS_SELECTOR, ".alert:last-child strong")  #константа для селектора цены товара в корзине
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert:first-child")  #константа для селектора сообщения об успешном добавлении в корзину

class BasePageLocators(): #создание класса BasePageLocators
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #константа для селектора ссылки на логин
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn-default")  #константа для селектора ссылки на корзину
    
class BasketPageLocators(): #создание класса BasketPageLocators (локаторы страницы корзины)
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items") #константа для селектора товара в корзине
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p") #константа для селектора сообщения о пустой корзине

    