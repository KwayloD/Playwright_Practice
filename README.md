## Практикуюсь писать UI автотесты на Python с Playwright для сайта: [QA Practice](https://www.qa-practice.com/).  
### Используемые библиотеки:  
Для работы кода понадобятся следующие библиотеки **Python**:  
- `pytest` — фреймворк для написания тестов
- `playwright` — фреймворк для написания UI тестов

**Перед началом работы установите библиотеки, используя команду:**
```
pip install -r requirements.txt
```

**А также установите браузеры для Playwright:**
```
playwright install
```

### Структура проекта:  
- **`pages/`** — содержит классы PageObject для страниц  
  - `base_page.py` — базовый класс с общими методами для всех страниц  
  - `home_page.py` —
  - `simple_button_page.py` —  
  - `text_input_page.py` —
- **`locators/`** — папка с файлом содержащем локаторы страниц
  - `locators.py` — файл с локаторами элементов для страниц
- **`tests/`** — включает тестовые сценарии:  
  - `conftest.py` — фикстуры для запуска браузера и страниц
  - `test_home_page.py` — тест главной страницы 
  - `test_simple_button_page.py` — тест страницы "Buttons"  
  - `test_text_input_page.py` — тест страницы "Input field  
- **`requirements.txt`** — список зависимостей проекта  
- **`README.md`** — описание проекта  