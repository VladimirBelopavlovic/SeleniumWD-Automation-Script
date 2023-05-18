
import pytest
from AutomationProjectWooCom.src.pages.HomePage import HomePage
from AutomationProjectWooCom.src.pages.Header import Header
from AutomationProjectWooCom.src.pages.CartPage import CartPage
from AutomationProjectWooCom.src.pages.CheckoutPage import CheckoutPage
from AutomationProjectWooCom.src.pages.OrderReceivedPage import OrderReceivedPage
from AutomationProjectWooCom.src.configs.generic_configs import GenericConfigs
from AutomationProjectWooCom.src.helpers.database_helpers import get_order_from_db_by_order_no


@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGuestUser:

    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):

        home_p = HomePage(self.driver)
        header = Header(self.driver)
        cart_p = CartPage(self.driver)
        checkout_p = CheckoutPage(self.driver)
        order_received_p = OrderReceivedPage(self.driver)

        home_p.go_to_home_page()

        home_p.click_first_add_to_cart_button()

        header.wait_until_cart_item_count(1)

        header.click_on_cart_on_right_header()
        product_names = cart_p.get_all_product_names_in_cart()
        assert len(product_names) == 1, f"Expected 1 item in cart but found {len(product_names)}"

        coupon_code = GenericConfigs.FREE_COUPON
        cart_p.apply_coupon(coupon_code)

        cart_p.click_on_proceed_to_checkout()

        checkout_p.fill_in_billing_info()
        checkout_p.click_place_order()

        order_received_p.verify_order_received_page_loaded()

        order_no = order_received_p.get_order_number()
        print('*********')
        print(order_no)
        print('*********')

        # db_order = get_order_from_db_by_order_no(order_no)
        # assert db_order, f"After creating order with FE, not found in DB." \
        #                  f"Order no:{order_no}"
        #
        # print("")
        # print("*******")
        # print("PASS")
        # print("*******")
