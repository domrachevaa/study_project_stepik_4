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
