from collections.abc import Sequence

from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: Chrome):
        self.driver = driver
        self.BASE_URL = 'https://google.com'

    def go_to_site(self):
        self.driver.get(self.BASE_URL)

    def find_element(self, locator: Sequence[str, str]):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator),
                                                    message=f"Can't find element by locator {locator}")
                                                    