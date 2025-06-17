from selenium.webdriver.common.by import By

class SearchPageLocators:
    input_field = (By.ID, "query")
    search_button = (By.XPATH, ".//button[contains(@class, 'btn-danger')]")
    clear_button = (By.XPATH, ".//button[contains(@class, 'btn-secondary')]")
    title_search_results = (By.XPATH, ".//h2[i[@class='fas fa-list text-primary']]//text()[contains(., 'Результаты поиска')]")
    clients_cards = (By.XPATH, ".//div[contains(@class, 'g-4')]")
    client_not_found_title = (By.XPATH, ".//div[@class='text-center py-5']//h4[text()='Клиенты не найдены']")
