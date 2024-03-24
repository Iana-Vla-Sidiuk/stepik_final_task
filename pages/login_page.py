from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage): #создание класса LoginPage (страница логина) - наследника класса BasePage
    def should_be_login_page(self):   # метод проверки логина (состоит из вызова трех методов - трех проверок)
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):  # метод проверки наличия подстроки "login" в текущем url браузера
        current_url = self.browser.current_url
        assert "/login" in current_url, "Login url is not presented"

    def should_be_login_form(self): # метод проверки наличия формы логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self): # метод проверки наличия формы регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"



