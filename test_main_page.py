from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"

# Проверка существования ссылки для входа на сайт и переход по ней
@pytest.mark.login_guest
class TestLoginFromMainPage():                    
    def test_guest_can_go_to_login_page(self, browser):   
        page = MainPage(browser, link)   
        page.open()                      
        page.go_to_login_page()          
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

# Проверка пустоты корзины при переходе с главной страницы
@pytest.mark.basket_guest
class TestEmptyBasketFromMainPage():
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, link)   
        page.open()                      
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_msg_basket_empty()
        basket_page.should_be_item_basket_empty()

    def test_guest_should_see_basket_button(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


