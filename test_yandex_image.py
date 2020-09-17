import pytest
from urllib.parse import parse_qs

from method_tests import MethodPage, Buffer

from selenium.webdriver.common.keys import Keys


def test_image_link(browser):
    """Поиск ссылки Картинки на главной странице yandex

    Args:
        browser (fixture): запуск браузера
    """
    yandex_main = MethodPage(browser)
    yandex_main.go_to_site()

    assert 'Картинки' == yandex_main.search_link('Картинки').text


def test_go_yandex_images(browser):
    """Проверка осуществился ли переход по ссылке
    """
    yandex_main = MethodPage(browser)
    yandex_main.go_to_tab_link('Картинки')

    assert 'https://yandex.ru/images/' in yandex_main.get_url()


def test_click_category_image(browser):
    """Проверка открытия первой категории изображений и верности запроса в поисковой строке
    """
    yandex_main = MethodPage(browser)

    yandex_main.find_elements_class('PopularRequestList-Item')[0].click()

    assert 'text' in yandex_main.get_url()
    assert yandex_main.find_element_class('input__control').get_attribute('value') == parse_qs(yandex_main.get_url())['text'][0]


def test_open_image(browser):
    """Проверка открытия первого изображения в коллекции
    """
    yandex_main = MethodPage(browser)
    result = yandex_main.find_elements_class('serp-item__link')
    result[0].click()

    assert parse_qs(yandex_main.get_url())['img_url']


def test_next_image(browser):
    """Проверка переключения на следующее изображение при помощи клавиш клавиатуры
    """
    yandex_main = MethodPage(browser)
    Buffer.IMAGE_ADDRESS = parse_qs(yandex_main.get_url())['img_url'][0]

    yandex_main.action_keyboard(Keys.ARROW_RIGHT)

    assert parse_qs(yandex_main.get_url())['img_url'][0] != Buffer.IMAGE_ADDRESS


def test_preview_image(browser):
    """Проверка переключения на предыдущее изображение при помощи клавиш клавиатуры
    """
    yandex_main = MethodPage(browser)

    yandex_main.action_keyboard(Keys.ARROW_LEFT)

    assert parse_qs(yandex_main.get_url())['img_url'][0] == Buffer.IMAGE_ADDRESS
