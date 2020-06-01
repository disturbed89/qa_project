import pytest
from .pages.product_page import ProductPage

link_sh = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
link_offer = "/?promo=offer"
link2 = link_sh + link_offer + "1"

@pytest.mark.parametrize('link_offer_num', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, link_offer_num):
    link = link_sh + link_offer + link_offer_num
    page = ProductPage(browser, link)  
    page.open()                     
    page.add_to_basket()

@pytest.mark.test4_3
@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basketbrowser(browser):
    page = ProductPage(browser, link2)  
    page.open()                     
    page.add_to_basket()
    page.should_not_be_success_message_is_not_element_present()

@pytest.mark.test4_3
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link2)  
    page.open()           
    page.should_not_be_success_message_is_not_element_present()

@pytest.mark.test4_3
@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link2)  
    page.open()                     
    page.add_to_basket()
    page.should_not_be_success_message_is_disappeared()

@pytest.mark.test4_8
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.test4_8
def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()