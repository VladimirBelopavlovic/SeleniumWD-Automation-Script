

import pytest
from AutomationProjectWooCom.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    @pytest.mark.tcid12
    def test_login_none_existing_user(self):

        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username('adksjadhsa')
        my_account.input_login_password('hjsakdsah')
        my_account.click_login_button()

        expected_err = 'Error: The username adksjadhsa is not registered on this site. If you are unsure of your username, try your email address instead.'
        my_account.wait_until_error_is_displayed(expected_err)
