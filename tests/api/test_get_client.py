import requests
import allure
from config.config import Config
import pytest

@allure.suite("API получения информации о клиенте")
@allure.sub_suite("GET /api/search?q={query}")
class TestGetClient:
    @allure.title("Получение пользователя")
    @allure.title("Получение информации о пользователе при вводе валидных значений")
    @pytest.mark.parametrize("search_value", [
        "Иванов",
        "1234567890",
        "ivanov@example.com",
        "+7(999)890-12-34"
    ])
    def test_get_client(self, search_value):
        response = requests.get(Config.get_clients(search_value))
        with allure.step("Проверка статус-кода"):
            assert response.status_code == 200
        response_json = response.json()
        with allure.step("Проверка, что список с клиентами не пустой"):
            assert len(response_json["data"])> 0
            assert response_json["status"] == "success"

    @allure.title("Получение информации о конкретном пользователе")
    def test_name_in_all_clients(self):
        search_value = "Петров"
        response = requests.get(Config.get_clients(search_value))
        response_json = response.json()
        assert "data" in response_json
        data = response_json["data"]
        with allure.step("Проверка, что все пользователи в данных содержат искомое имя"):
            for client in data:
                client_name = client["name"]
                assert search_value in client_name, f"Имя '{search_value}' не найдено в {client_name}"

    @allure.title("Проверка поиска клиента с именем, которого нет в базе")
    def test_name_not_found(self):
        search_value = "Киров"
        response = requests.get(Config.get_clients(search_value))
        with allure.step("Проверка статус-кода"):
            assert response.status_code == 404
        with allure.step("Проверка, что статус в ответе соответствует ошибке"):
            response_json = response.json()
            assert response_json["status"] == "error"




