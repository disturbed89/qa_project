from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_msg_basket_empty(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*BasketPageLocators.BASKET_MSG), "Msg from basket empty not found"

    def should_be_item_basket_empty(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Items from basket not found"
