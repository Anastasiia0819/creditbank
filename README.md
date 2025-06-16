# API + UI tests for creditbank
Тестовый проект по автоматизации тестирования API и UI для сервиса **creditbank**.

# Ссылки
[Веб-приложение] (http://37.203.243.26:5000)

## Стек технологий

- Python 3.10+
- `pytest` — фреймворк для запуска тестов
- `requests` — HTTP-клиент для взаимодействия с API
- `selenium` — автоматизация UI-тестирования (браузерное взаимодействие)
- `allure` — отчетность
- `pytest-html` — для генерации HTML-отчета

## Стек технологий

## Структура проекта
```bash
├── config/                  # Конфигурационные файлы
│   └── config.py            # Общие настройки (URLs, токены и т.д.)
│
├── locators/                # Локаторы для UI тестов
│   ├── __init__.py
│   ├── main_page_locator.py        # Локаторы для главной страницы 
│   └── search_page_locator.py # Локаторы для страницы поиска
│
├── pages/                   # Страницы для UI тестов (Page Object Model)
│   ├── __init__.py
│   ├── main_page.py        # Класс главной страницы
│   └── search_page.py # Класс страницы поиска
│
├── tests/                   # Директория для тестов
│   ├── ui/                  # UI тесты (Selenium)
│   │   ├── __init__.py
│   │   ├── test_search_ui.py    # Пример UI теста для поиска клиентов
│   │
│   ├── api/                 # API тесты (requests или Playwright)
│   │   ├── __init__.py
│   │   ├── test_search_api.py     # Пример API теста для поиска клиентов
│   │
│   └── test_all.py          # Главный файл для запуска всех тестов
│
├── reports/                 # Папка для отчетов
│   └── allure-results/      # Результаты для Allure
│
├── requirements.txt         # Файл с зависимостями
├── pytest.ini               # Конфигурация для pytest
└── README.md                # Документация по проекту


