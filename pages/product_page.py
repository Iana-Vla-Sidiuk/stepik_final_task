from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage): #создание класса ProductPage (страница товара) - наследника класса BasePage
    def add_product_to_cart(self):  # метод проверки наличия кнопки добавления в корзину и добавления товара в корзину
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "Add to cart is not presented"
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def get_name(self):  #метод получения названия товара
        name_element = self.browser.find_element(*ProductPageLocators.NAME)
        name = name_element.text
        return name

    def get_price(self):  #метод получения цены товара
        price_element = self.browser.find_element(*ProductPageLocators.PRICE)
        price = price_element.text
        return price

    def should_be_right_name(self, name):  #метод проверки совпадения названия товара в корзине
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        assert book_name.text == name, "Incorrect book name"

    def should_be_right_price(self, price):  #метод проверки совпадения цены товара в корзине
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        assert book_price.text == price, "Incorrect book price"