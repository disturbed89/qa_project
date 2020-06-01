from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес 
        assert "login" in self.browser.current_url, "The 'login' substring is missing from the current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login Form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration Form is not presented"

    def register_new_user(self, email, password):
        # регистрируем нового пользователя
        input_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        input_email.send_keys(email) 
        input_pass1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        input_pass1.send_keys(password) 
        input_pass2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        input_pass2.send_keys(password) 
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        reg_button.click()


