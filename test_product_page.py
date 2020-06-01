import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage




# Проверка Акции при добавлении в корзину
@pytest.mark.basket_from_quiz
class TestBasketFromQuiz():
    @pytest.mark.need_review
    @pytest.mark.parametrize('link_offer_num', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
    def test_guest_can_add_product_to_basket(self, browser, link_offer_num):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer" + link_offer_num
        page = ProductPage(browser, link)  
        page.open()                     
        page.add_to_basket_quiz()


# Проверка отсутствия эллемента различными способами
@pytest.mark.cant_see_message
class TestProductCant():
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_cant_see_success_message_after_adding_product_to_basketbrowser(self, browser):
        page = ProductPage(browser, self.link)  
        page.open()                     
        page.add_to_basket()
        page.should_not_be_success_message_is_not_element_present()

    def test_guest_cant_see_message(self, browser):
        page = ProductPage(browser, self.link)  
        page.open()           
        page.should_not_be_success_message_is_not_element_present()

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)  
        page.open()                     
        page.add_to_basket()
        page.should_not_be_success_message_is_disappeared()


# Проверка перехода на страницу логина со страницы товара
@pytest.mark.login_guest
class TestLoginFromProductPage():
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_login_link()
    
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page (self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_login_page()


# Проверка пустоты корзины при переходе со страницы товара
@pytest.mark.basket_guest
class TestEmptyBasketFromProductPage():
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_msg_basket_empty()
        basket_page.should_be_item_basket_empty()


# Регистрация пользователя и добавление в корзину
@pytest.mark.login_user
class TestUserAddToBasketFromProductPage(): 
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/" 
    #регистрация пользователя
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = ProductPage(browser, self.link)   
        self.page.open()                      
        self.page.go_to_login_page()          
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        email = str(time.time()) + "@fakemail.org"
        login_page.register_new_user(email, "fsdgfwefsdfw")
        login_page.should_be_authorized_user()

    def test_user_cant_see_message(self, browser):
        page = ProductPage(browser, self.link)  
        page.open()           
        page.should_not_be_success_message_is_not_element_present()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)  
        page.open()              
        page.add_to_basket()
