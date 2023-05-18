import pytest
import os

env_var = os.environ
os.environ['BROWSER'] = 'chrome'


@pytest.mark.usefixtures("init_driver")
class TestDummy:

    def test_dummy_func(self):
        print("I am dummy test line 1")
        print("I am dummy test line 2")
        self.driver.get("https://supersqa.com")
        import pdb; pdb.set_trace()
