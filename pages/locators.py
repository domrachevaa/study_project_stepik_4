from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    reg_form = (By.CSS_SELECTOR, "form#register_form")
    '''reg_email = (By.CSS_SELECTOR, 'input[name="registration-email"')
    reg_password = (By.CSS_SELECTOR, 'input[name="registration-password1"')'''

    login_form = (By.CSS_SELECTOR, "form#login_form")
    '''login_email = (By.CSS_SELECTOR, 'input[name="login-username"]')
    login_password = (By.CSS_SELECTOR, 'input[name="login-password"]')'''


class ProductPageLocators:
    btn_add_to_basket = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    product_name = (By.CSS_SELECTOR, ".product_main h1")
    product_in_basket = (By.CSS_SELECTOR, '.alert-success:first-child strong')
    price_added_in_basket = (By.CSS_SELECTOR, '.alertinner p strong')
    price = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    btn_basket = (By.CSS_SELECTOR, "span a.btn-default")


class BasketPageLocators:
    basket_empty = (By.CSS_SELECTOR, ".content p")
    basket_empty_end = (By.CSS_SELECTOR, ".content p a")
    basket_content = (By.CSS_SELECTOR, ".basket_summary")
