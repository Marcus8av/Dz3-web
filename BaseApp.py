from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import yaml


with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    url = testdata['url']
    url_login = testdata['url_login']

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = url

    def find_element(self, locator, times=10):
        return WebDriverWait(self.driver, times).until(expected_conditions.presence_of_element_located(locator), message=f"элемент {locator} не найден")

    def get_element_property(self, mode, locator, property):
        element = self.find_element(mode, locator)
        return element.value_of_css_property(property)

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def get_alert_text(self):
        alert = self.driver.switch_to.alert.text
        return alert