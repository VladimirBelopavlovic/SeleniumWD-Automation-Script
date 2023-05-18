
from AutomationProjectWooCom.src.SeleniumExtended import SeleniumExtended
from AutomationProjectWooCom.src.pages.locators.HeaderLocators import HeaderLocators


class Header(HeaderLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def click_on_cart_on_right_header(self):
        self.sl.wait_and_click(self.CART_RIGHT_HEADER)

    def wait_until_cart_item_count(self, count):
        expected_text = str(count) + ' item'
        self.sl.wait_until_element_contains_text(self.CART_ITEM_COUNT, expected_text)
