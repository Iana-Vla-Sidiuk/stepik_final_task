from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

class BasePage(): #создание класса BasePage
    def __init__(self, browser, url, timeout=10): #конструктор BasePage
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self): #метод открытия страницы в браузере
        self.browser.get(self.url)

    def is_element_present(self, how, what): #метод проверки наличия элемента с обработкой исключения
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4): #метод проверки отсутствия элемента с явным ожиданием
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4): #метод проверки того, что элемент исчезает, с явным ожиданием
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self): #метод расчета результата математического выражения для получения проверочного кода
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")




