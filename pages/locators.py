from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    reg_form = (By.CSS_SELECTOR, "form#register_form")
    '''reg_email = (By.CSS_SELECTOR, 'input[name="registration-email"')
    reg_password = (By.CSS_SELECTOR, 'input[name="registration-password1"')'''

    login_form = (By.CSS_SELECTOR, "form#login_form")
    '''login_email = (By.CSS_SELECTOR, 'input[name="login-username"]')
    login_password = (By.CSS_SELECTOR, 'input[name="login-password"]')'''


