from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage): #создание класса BasketPage (страница корзины) - наследника класса BasePage
    def should_be_empty_basket(self): #метод проверки отсутствия товаров в корзине
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Basket is not empty, but should be"

    def should_be_empty_basket_message(self): #метод проверки наличия сообщения о пустой корзине
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty basket message is not presented"
