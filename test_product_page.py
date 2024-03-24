from .pages.product_page import ProductPage

#тест проверки добавления товара в корзину, соответствия названия и цены товара в корзине
def test_guest_can_add_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    # инициализируем Page Object, передаем в конструктор класса ProductPage(страницы товара) экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
    page.open()                           # открываем страницу
    page.add_product_to_cart()            # проверяем наличие кнопки добавления в корзину и добавляем товар в корзину
    page.solve_quiz_and_get_code()        # рассчитываем результат математического выражения для получения проверочного кода
    name = page.get_name()                # получаем имя товара и сохраняем в переменную
    price = page.get_price()              # получаем цену товара и сохраняем в переменную
    page.should_be_right_name(name)       # проверяем совпадение названия товара в корзине
    page.should_be_right_price(price)     # проверяем совпадение цены товара в корзине


    
    
    
