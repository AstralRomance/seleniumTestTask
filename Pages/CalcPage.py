import pytest
from multiprocessing.sharedctypes import Value
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class CalcFormFieldsLocators:
    RESULT_PANEL = (By.CLASS_NAME, 'qv3Wpe')
    MEMORY_PANEL = (By.CLASS_NAME, 'vUGUtc')

class CalcAutoPage(BasePage):
    operators_locator = {'+': 'tr:nth-child(5) .mF5fo > .MEdqYd',
                         '-': 'tr:nth-child(4) .mF5fo > .XRsWPe',
                         '*': 'tr:nth-child(3) .mF5fo > .XRsWPe',
                         '/': 'tr:nth-child(2) .mF5fo > .XRsWPe',
                         '=': '.UUhRt'}

    def get_number_selector(self, target_num: int) -> str:
        return f'tr:nth-child(4) > td:nth-child({target_num}) > .A2W7l > .XRsWPe'
        
    def get_operator_locator(self, operator: str) -> str:
        operator_locator = CalcAutoPage.operators_locator.get(operator)
        if not operator_locator:
            raise ValueError('Invalid operator. This input is invalid or not supported.')
        return operator_locator

    def input_calc_expression(self, expr: str) -> None:
        target_expr = expr.replace(' ', '')
        for sym in target_expr:
            if sym.isdigit():
                target_selector_str = self.get_number_selector(sym)
            else:
                target_selector_str = self.get_operator_locator(sym)
            if not target_selector_str:
                raise ValueError(f'{sym} is invalid or not supported.')
            target_selector = (By.CSS_SELECTOR, target_selector_str)
            self.find_element(target_selector).click()
        self.find_element((By.CSS_SELECTOR, self.get_operator_locator('='))).click()

    def get_result_field(self) -> int:
        result_selector = self.find_element(CalcFormFieldsLocators.RESULT_PANEL)
        try:
            result_val = int(result_selector.text)
        except ValueError:
            pytest.fail(f'Invalid result field: {result_selector.text}')
        return result_val

    def get_memory_panel(self):
        memory_panel = self.find_element(CalcFormFieldsLocators.MEMORY_PANEL)
        return memory_panel.text
