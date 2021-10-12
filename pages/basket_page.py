from .base_page import BasePage
from .locators import BasketPageLocators
import re


class BasketPage(BasePage):
    def should_be_title(self):
        languages = {
            "ar": "سلة التسوق فارغة",
            "ca": "La seva cistella està buida.",
            "cs": "Váš košík je prázdný.",
            "da": "Din indkøbskurv er tom.",
            "de": "Ihr Warenkorb ist leer.",
            "en-gb": "Your basket is empty.",
            "el": "Το καλάθι σας είναι άδειο.",
            "es": "Tu carrito esta vacío.",
            "fi": "Korisi on tyhjä",
            "fr": "Votre panier est vide.",
            "it": "Il tuo carrello è vuoto.",
            "ko": "장바구니가 비었습니다.",
            "nl": "Je winkelmand is leeg",
            "pl": "Twój koszyk jest pusty.",
            "pt": "O carrinho está vazio.",
            "pt-br": "Sua cesta está vazia.",
            "ro": "Cosul tau este gol.",
            "ru": "Ваша корзина пуста",
            "sk": "Váš košík je prázdny",
            "uk": "Ваш кошик пустий.",
            "zh-hans": "Your basket is empty."
        }
        getting_link = self.browser.current_url
        a = re.findall(r"com/([\D]*?)/", getting_link)[0]
        print('Language from URL:', a)
        just_text = self.browser.find_element(*BasketPageLocators.basket_empty).text.replace(
            self.browser.find_element(*BasketPageLocators.basket_empty_end).text, ''
        )

        assert languages.get(a) in just_text, "Error checking the text of an empty basket"

    def should_be_empty(self):
        assert self.is_disappeared(*BasketPageLocators.basket_content), "Something in basket"
