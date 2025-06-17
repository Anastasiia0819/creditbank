from selenium.webdriver.chrome.webdriver import WebDriver
from locators.search_page_locators import SearchPageLocators
import allure
from pages.base_page import BasePage

class SearchPage(BasePage):
    @allure.step('Ожидание кликабельности кнопки "Найти"')
    def wait_search_button(self):
        self.wait_for_element_visible(SearchPageLocators.search_button)
        self.wait_element_to_be_clickable(SearchPageLocators.search_button)

    def click_search_button(self):
        self.click_element(SearchPageLocators.search_button)

    @allure.step('Вставить значение в поле ввода"')
    def enter_value_field(self, value):
        self.enter_value(SearchPageLocators.input_field, value)

    def clear_field_search_page(self):
        self.clear_search_input(SearchPageLocators.input_field)

    #Получить значение из поля ввода
    def get_input_value(self):
        return self.find_element(SearchPageLocators.input_field).get_attribute("value")

    def find_card_clients(self):
        return self.find_elements(SearchPageLocators.clients_cards)

    #Проверка наличия карточек клиентов на странице
    def is_card_clients_displayed(self):
        cards = self.find_card_clients()
        return len(cards) > 0  # Если карточки есть, возвращаем True

    #Заголовок "Клиенты не найдены"
    def client_not_found_title(self):
        self.wait_for_element_visible(SearchPageLocators.client_not_found_title)
        try:
            return self.find_element(SearchPageLocators.client_not_found_title)
        except Exception as e:
            print(f"Ошибка: {e}")
            return None






