import requests
import pytest
from selenium import webdriver
from config.config import Config

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # не открывает браузер
    chrome = webdriver.Chrome(options=options)
    chrome.maximize_window()
    chrome.get(Config.URL)
    yield chrome
    chrome.quit()
