from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login/" in self.browser.current_url, "/login/ not in URL this page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), "Log_in form not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.reg_form), "Registration form not found"

    def should_be_register_form_with_simple_elements(self):
        assert self.is_element_present(*LoginPageLocators.reg_email) and self.is_element_present(
            *LoginPageLocators.reg_password1) and self.is_element_present(*LoginPageLocators.reg_password2) and \
               self.is_element_present(*LoginPageLocators.reg_btn), "Not all fields are presented in the form"

    def register_new_user(self, email, password):
        self.should_be_register_form_with_simple_elements()
        self.browser.find_element(*LoginPageLocators.reg_email).\
            send_keys(email)
        self.browser.find_element(*LoginPageLocators.reg_password1).\
            send_keys(password)
        self.browser.find_element(*LoginPageLocators.reg_password2).\
            send_keys(password)
        self.browser.find_element(*LoginPageLocators.reg_btn).\
            click()
