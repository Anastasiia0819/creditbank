from selenium.webdriver.chrome.webdriver import WebDriver
from locators.main_page_locators import MainPageLocators
import allure
from pages.base_page import BasePage
from config.config import Config

class MainPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_main_page(self):
        self.navigate(Config.URL)

    @allure.step('Ожидание кликабельности кнопки "Поиск" в header')
    def wait_search_client_button_header(self):
        self.wait_for_element_visible(MainPageLocators.search_clients_header_button)
        self.wait_element_to_be_clickable(MainPageLocators.search_clients_header_button)

    @allure.step('Ожидание кликабельности кнопки "Поиск" на странице')
    def wait_search_client_button_page(self):
        self.wait_for_element_visible(MainPageLocators.search_clients_button)
        self.wait_element_to_be_clickable(MainPageLocators.search_clients_button)

    @allure.step('Клик на кнопку "Поиск клиентов" в header')
    def click_search_client_button_header(self):
        self.click_element(MainPageLocators.search_clients_header_button)

    @allure.step('Клик на кнопку "Поиск клиентов" на страницe')
    def click_search_client_button_page(self):
        self.click_element(MainPageLocators.search_clients_button)

