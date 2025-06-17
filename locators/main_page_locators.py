from selenium.webdriver.common.by import By

class MainPageLocators:
    search_clients_button = (By.XPATH, ".//a[contains(@class, 'btn-primary')]")
    search_clients_header_button = (By.XPATH, ".//a[@class='nav-link' and @href='/search']")
