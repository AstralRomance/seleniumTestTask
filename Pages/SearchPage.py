from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class SearchLocators:
    SEARCH_FIELD_LOCATION = (By.CSS_SELECTOR, '.gLFyf')
    SEARCH_BUTTON_LOCATION = (By.CLASS_NAME, 'gNO89b')


class SearchPage(BasePage):
    def search_request_input(self, search_string):
        print(SearchLocators.SEARCH_FIELD_LOCATION)
        search_field = self.find_element(SearchLocators.SEARCH_FIELD_LOCATION)
        search_field.send_keys(search_string)

    def run_search(self):
        return self.find_element(SearchLocators.SEARCH_BUTTON_LOCATION).submit()
