from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webdriver import WebDriver
import allure

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    @allure.step('Проверка актуальности url')
    def get_current_url_base(self):
        return self.driver.current_url

    def find_element(self, locator, timeout=10):
         return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_all_elements_located(locator))

        # клик на элемент
    def click_element(self, locator, timeout=10):
        self.find_element(locator, timeout).click()

        # вставить текст в поле
    def enter_value(self, locator, text, timeout=10):
        self.find_element(locator, timeout).send_keys(text)

        # ожидание элемента
    def wait_for_element_visible(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

        # ожидание кликабельности элемента
    def wait_element_to_be_clickable(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    #очистка поля ввода
    def clear_search_input(self, locator, timeout=10):
        self.find_element(locator,timeout).clear()


