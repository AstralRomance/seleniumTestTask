import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope='session')
def create_browser():
    chrome_browser = Chrome()
    chrome_browser.maximize_window()
    yield chrome_browser
    chrome_browser.quit()

@pytest.fixture
def calc_input():
    yield '1 * 2 - 3 + 1'
