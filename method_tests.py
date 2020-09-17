from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Buffer():
    IMAGE_ADDRESS = ''


class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://yandex.ru/'

    def find_element_id(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located((By.ID, locator)), message=f"Can't find element by locator {locator}")

    def find_element_class(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, locator)), message=f"Can't find element by locator {locator}")

    def find_elements_class(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, locator)), message=f"Can't find element by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def go_to_tab(self):
        tabs = self.driver.window_handles
        return self.driver.switch_to.window(tabs[1])

    def get_url(self):
        import time
        time.sleep(1)
        return self.driver.current_url

    def search_link(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, locator)), message=f"Can't find element by locator {locator}")


class MethodPage(BasePage):

    def search_element(self):
        return self.find_element_id('text')

    def search_field(self):
        input_field = self.find_element_id('text')
        input_field.click()
        return input_field

    def go_to_tab_link(self, word):
        self.search_link(word).click()
        return self.go_to_tab()

    def action_keyboard(self, button):
        action = ActionChains(self.driver)
        return action.key_down(button).key_up(button).perform()