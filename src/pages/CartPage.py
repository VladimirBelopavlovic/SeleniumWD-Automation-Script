
from AutomationProjectWooCom.src.SeleniumExtended import SeleniumExtended
from AutomationProjectWooCom.src.pages.locators.CartPageLocators import CartPageLocators


class CartPage(CartPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_cart_page(self):
        pass

    def get_all_product_names_in_cart(self):

        product_name_elements = self.sl.wait_and_get_elements(self.PRODUCT_NAMES_IN_CART)
        product_names = [i.text for i in product_name_elements]

        return product_names

    def input_coupon(self, coupon_code):
        self.sl.wait_and_input_text(self.COUPON_FIELD, coupon_code)

    def click_apply_coupon(self):
        self.sl.wait_and_click(self.APPLY_COUPON_BTN)

    def apply_coupon(self, coupon_code):
        self.input_coupon(coupon_code)
        self.click_apply_coupon()
        success_msg = self.get_displayed_message()
        assert success_msg == 'Coupon code applied successfully.', f"Unexpected " \
                    f"Message when applying coupon."

    def get_displayed_message(self):
        txt = self.sl.wait_and_get_text(self.CART_PAGE_MESSAGE)
        return txt

    def click_on_proceed_to_checkout(self):
        self.sl.wait_and_click(self.PROCEED_TO_CHECKOUT_BTN)



