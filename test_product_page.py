import time
import pytest

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
link2 = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"


@pytest.mark.need_review
@pytest.mark.parametrize('no', [i for i in range(10)])
@pytest.mark.xfail
def test_guest_can_add_product_to_basket(browser, no):
    link = f"{link1}?promo=offer{no}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_btn()
    page.add_to_btn()
    page.solve_quiz_and_get_code()
    page.should_be_one_name()
    page.should_be_one_price()


@pytest.mark.need_review
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.should_be_btn()
    page.add_to_btn()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.should_be_btn()
    page.add_to_btn()
    page.should_not_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.should_be_basket()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty()
    basket_page.should_be_title()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.register_new_user(
            str(time.time()) + "@fakemail.org", "exRd0PR2T"
        )
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f"{link1}?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_btn()
        page.add_to_btn()
        page.solve_quiz_and_get_code()
        page.should_be_one_name()
        page.should_be_one_price()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link1)
        page.open()
        page.should_not_be_success_message()
