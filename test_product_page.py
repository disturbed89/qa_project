import pytest
from .pages.product_page import ProductPage

link_sh = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
link_offer = "/?promo=offer"

@pytest.mark.parametrize('link_offer_num', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, link_offer_num):
    link = link_sh + link_offer + link_offer_num
    page = ProductPage(browser, link)  
    page.open()                     
    page.should_be_basket()

