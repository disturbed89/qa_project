from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        self.should_be_button_add_basket()
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.click_button_add_to_basket()
        self.check_text_in_alert(name, "product name check")
        self.check_text_in_alert(price, "product price check")

    def add_to_basket_quiz(self):
        self.should_be_button_add_basket()
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.click_button_add_to_basket()
        self.solve_quiz_and_get_code()
        self.check_text_in_alert(name, "product name check")
        self.check_text_in_alert(price, "product price check")

    def should_not_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_not_be_success_message_is_not_element_present(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_button_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_BASKET), "Button Add to Basket is not presented"

    def click_button_add_to_basket(self):
        button_link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        button_link.click() 
    
    def check_text_in_alert(self, ch_text, msg):
        message_result_comp = self.browser.find_elements(*ProductPageLocators.RES_BASKET)
        message_result = []
        for i in range(len(message_result_comp)):
            message_result.append(message_result_comp[i].text)        
        assert ch_text in message_result, f"The {msg} '{ch_text}' differs"