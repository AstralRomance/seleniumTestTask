import time

from Pages.SearchPage import SearchPage
from Pages.CalcPage import CalcAutoPage


class TestCalcPage:
    def test_chrome_calc(self, create_browser, calc_input):
        google_main_page = SearchPage(create_browser)
        google_main_page.go_to_site()
        google_main_page.search_request_input('Калькулятор')
        google_main_page.run_search()

        calc_page = CalcAutoPage(create_browser)
        calc_page.input_calc_expression(calc_input)

        time.sleep(0.1)
        create_browser.save_screenshot('calculation.png')

        calc_res = calc_page.get_result_field()
        assert calc_res == 0
        calc_memory = calc_page.get_memory_panel()
        assert calc_memory == '1 * 2 - 3 + 1 ='
