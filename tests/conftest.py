import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:  # Запускает движок Playwright
        browser = p.chromium.launch(headless=False, slow_mo=500)  # Открывает Chromium в headed-режиме (c UI)
        #browser = p.chromium.launch(headless=True)  # Открывает Chromium в headless-режиме (без UI)
        yield browser  # Передаёт объект браузера в тесты
        browser.close()  # После завершения всех тестов — закрывает браузер

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()  # Создаёт новый контекст (изолированная "сессия" браузера)
    page = context.new_page()  # Открывает новую вкладку
    yield page  # Передаёт страницу в тест
    context.close()  # После теста — закрывает вкладку и её контекст