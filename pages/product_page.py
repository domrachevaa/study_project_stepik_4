from .base_page import BasePage
from .locators import ProductPageLocators
import pytest


class ProductPage(BasePage):
    def should_be_btn(self):
        assert self.is_element_present(*ProductPageLocators.btn_add_to_basket)

    @pytest.mark.xfail
    def add_to_btn(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.btn_add_to_basket)
        add_to_basket.click()

    def should_be_one_name(self):
        assert self.browser.find_element(*ProductPageLocators.product_name).text == self.browser.find_element(
            *ProductPageLocators.product_in_basket).text, 'Product name and added in basket product are different'

    def should_be_one_price(self):
        assert self.browser\
                   .find_element(*ProductPageLocators.price).text\
               == self.browser.find_element(*ProductPageLocators.price_added_in_basket).text,\
        'Price and value added to basket are different'

