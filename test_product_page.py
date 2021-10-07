import time

from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_btn()
    page.add_to_btn()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.should_be_one_name()
    page.should_be_one_price()


