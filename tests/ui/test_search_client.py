from config.config import Config
import allure
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.search_page import SearchPage
import pytest
import time

class TestSearchClient:
    @allure.feature("Функциональность поиска")
    @allure.title("Проверка поиска по имени, паспорту, телефону или email")
    @pytest.mark.parametrize("search_value", [
        "Иванов",
        "1234567890",  #Паспорт
        "(999)123-45-67",
        "volkova@example.com"
    ])
    def test_search_client(self, driver, search_value):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        search_page = SearchPage(driver)
        with allure.step("Клик на кнопку 'Перейти к поиску'"):
            main_page.open_main_page()
            main_page.wait_search_client_button_page()
            main_page.click_search_client_button_page()
            assert base_page.get_current_url_base() == Config.search_url
        with allure.step(f"Поиск по значению: {search_value}"):
            search_page.clear_field_search_page()
            search_page.enter_value_field(search_value)
            # Проверка, что длина введенного значения не более 5 символов
            entered_value = search_page.get_input_value()
            assert len(entered_value) == 5
            search_page.click_search_button()
        with allure.step("Проверка наличия карточек клиентов"):
            assert search_page.is_card_clients_displayed(), "Карточки клиентов не отображаются на странице."

    @allure.feature("Функциональность поиска")
    @allure.title("Проверка, что имя не найдено на странице с карточками клиентов")
    def test_name_not_found_in_client_cards(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        search_page = SearchPage(driver)
        with allure.step("Клик на кнопку 'Поиск клиентов' в хедере"):
            main_page.open_main_page()
            main_page.wait_search_client_button_header()
            main_page.click_search_client_button_header()
            assert base_page.get_current_url_base() == Config.search_url
        with allure.step(f"Проверка, что клиент не найден"):
            search_page.clear_field_search_page()
            search_page.enter_value_field("Киров")
            search_page.click_search_button()
            assert search_page.client_not_found_title()











