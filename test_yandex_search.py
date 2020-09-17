import pytest
import selenium

from method_tests import MethodPage

from selenium.webdriver.common.keys import Keys

def test_search_field(browser):
    yandex_main = MethodPage(browser)
    yandex_main.go_to_site()

    search_element = yandex_main.search_element()

    assert search_element.tag_name == "input"


def test_search_field_suggest(browser):
    yandex_main = MethodPage(browser)

    yandex_main.search_field().send_keys('тензор')

    assert yandex_main.find_element_class('mini-suggest__popup')

def test_search_by_word(browser):
    yandex_main = MethodPage(browser)

    yandex_main.search_field().send_keys(Keys.ENTER)
    result_search = yandex_main.find_elements_class('link_theme_outer')

    for url in result_search[:5]:
        assert 'tensor.ru' in url.find_element_by_tag_name('b').text