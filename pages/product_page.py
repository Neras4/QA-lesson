from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
    


class ProductPage(BasePage):
    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Button is not presented"
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def should_be_same_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_BASKET).text
        assert book_price == basket_price, 'Price is not the same'

    def should_be_same_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_basket_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME_BASKET).text
        assert book_name == book_basket_name, 'Name is not the same'
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
