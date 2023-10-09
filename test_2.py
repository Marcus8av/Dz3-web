import time
import pytest
from testpage import OperationHelper
username = 'Timka'
password = '625dea530b'

def test_2(browser):
    test_page1 = OperationHelper(browser)
    test_page1.go_to_site()
    test_page1.enter_login('Timka')
    test_page1.enter_password('625dea530b')
    test_page1.click_button()
    time.sleep(3)
    test_page1.click_contact()
    time.sleep(3)
    test_page1.enter_cont_name('Jorik')
    test_page1.enter_cont_email('moyou@mail.ru')
    test_page1.enter_cont_text('Nu ti i molodec')
    time.sleep(3)
    test_page1.click_button()
    time.sleep(3)
    assert test_page1.get_alert_text() == 'Form successfully submitted'