from playwright.sync_api import Page, expect
from utils.logger_utils import get_logger

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger()

    def log(self, message: str):
        self.logger.info(message)

    def log_exception(self, action: str, error: Exception):
        self.logger.exception(f"Ошибка при {action}: {error}")

    def open(self, url: str):
        self.log(f"Открываю страницу: {url}")
        try:
            self.page.goto(url)
        except Exception as e:
            self.log_exception(f"открытии страницы {url}", e)
            raise

    def get_inner_text(self, locator: str) -> str:
        self.log(f"Получение внутреннего текста элемента: {locator}")
        try:
            self.page.wait_for_selector(locator)
            element = self.page.locator(locator)
            text = element.inner_text().strip()
            self.log(f"Текст элемента: '{text}'")
            expect(element).to_be_visible()
            return text
        except Exception as e:
            self.log_exception(f"получении текста элемента {locator}", e)
            raise

    def get_text_content(self, locator: str, expected: str):
        self.log(f"Проверка, что элемент {locator} содержит текст: '{expected}'")
        try:
            self.page.wait_for_selector(locator)
            element = self.page.locator(locator)
            self.log(f"Текст найден: '{element.text_content().strip()}'")
            expect(element).to_have_text(expected.strip())
        except Exception as e:
            self.log_exception(f"проверке текста в элементе {locator}", e)
            raise

    def click(self, locator: str):
        self.log(f"Клик по элементу: {locator}")
        try:
            self.page.locator(locator).click()
        except Exception as e:
            self.log_exception(f"клике по элементу {locator}", e)
            raise

    def click_by_text(self, text: str):
        self.log(f"Клик по элементу с текстом: '{text}'")
        try:
            self.page.get_by_text(text, exact=True).click()
        except Exception as e:
            self.log_exception(f"клике по тексту '{text}'", e)
            raise

    def go_back(self,):
        self.log(f"Возврат на предыдущую страницу")
        try:
            self.page.go_back()
        except Exception as e:
            self.log_exception(f"возврате на предыдущую страницу", e)
            raise

    def fill(self, locator: str, text: str):
        self.log(f"Заполнение поля {locator} текстом: '{text}'")
        try:
            self.page.locator(locator).fill(text)
        except Exception as e:
            self.log_exception(f"вводе текста в {locator}", e)
            raise

    def fill_and_press_enter(self, locator: str, text: str):
        self.log(f"Ввод '{text}' в поле {locator} и нажатие Enter")
        try:
            self.page.locator(locator).fill(text)
            self.page.locator(locator).press("Enter")
        except Exception as e:
            self.log_exception(f"вводе текста и нажатии Enter в {locator}", e)
            raise

    def choose_value_in_select(self, locator: str, value: str):
        self.log(f"Выбор значения '{value}' в select {locator}")
        try:
            self.page.locator(locator).select_option(value=value)
        except Exception as e:
            self.log_exception(f"выборе значения '{value}'", e)
            raise

    def element_is_disabled(self, locator: str):
        self.log(f"Проверка, что элемент {locator} недоступен")
        try:
            expect(self.page.locator(locator)).to_be_disabled()
        except Exception as e:
            self.log_exception(f"проверке, что элемент {locator} недоступен", e)
            raise

    def element_is_enabled(self, locator: str):
        self.log(f"Проверка, что элемент {locator} доступен")
        try:
            expect(self.page.locator(locator)).to_be_enabled()
        except Exception as e:
            self.log_exception(f"проверке, что элемент {locator} доступен", e)
            raise

    def select_checkbox(self, locator: str):
        self.log(f"Отмечаем чекбокса: {locator}")
        try:
            self.page.locator(locator).check()
        except Exception as e:
            self.log_exception(f"отметке чекбокса {locator}", e)
            raise

    def deselect_checkbox(self, locator: str):
        self.log(f"Снимаем отметку с чекбокса: {locator}")
        try:
            self.page.locator(locator).uncheck()
        except Exception as e:
            self.log_exception(f"снятии отметки с чекбокса {locator}", e)
            raise

    def is_checkbox_selected(self, *locators: str):
        for locator in locators:
            self.log(f"Проверка, что чекбокс {locator} отмечен")
            try:
                expect(self.page.locator(locator)).to_be_checked()
            except Exception as e:
                self.log_exception(f"проверке чекбокса {locator}", e)
                raise

    def is_checkbox_deselected(self, *locators: str):
        for locator in locators:
            self.log(f"Проверка, что чекбокс {locator} не отмечен")
            try:
                expect(self.page.locator(locator)).not_to_be_checked()
            except Exception as e:
                self.log_exception(f"проверке чекбокса {locator}", e)
                raise

    def open_new_tab(self, locator: str) -> Page:
        self.log(f"Открытие новой вкладки через элемент: {locator}")
        try:
            with self.page.context.expect_page() as new_page_info:
                self.page.locator(locator).click()
            new_tab = new_page_info.value
            new_tab.wait_for_load_state()
            new_tab.bring_to_front()
            return new_tab
        except Exception as e:
            self.log_exception("открытии новой вкладки", e)
            raise

    def switch_to_tab(self, index: int) -> Page:
        self.log(f"Переключение на вкладку с индексом {index}")
        try:
            new_tab = self.page.context.pages[index]
            new_tab.bring_to_front()
            self.page = new_tab
            return new_tab
        except Exception as e:
            self.log_exception(f"переключении на вкладку {index}", e)
            raise

    def close_tab_by_index(self, index: int):
        self.log(f"Закрытие вкладки с индексом {index}")
        try:
            if index < len(self.page.context.pages):
                self.page.context.pages[index].close()
        except Exception as e:
            self.log_exception(f"закрытии вкладки {index}", e)
            raise

    def dialog_alert(self, locator: str, accept: bool = True, prompt_text: str = None):
        self.log(f"Обработка диалогового окна через элемент {locator}")
        try:
            def handle_dialog(dialog):
                if dialog.type == "prompt" and prompt_text:
                    dialog.accept(prompt_text) if accept else dialog.dismiss()
                elif accept:
                    dialog.accept()
                else:
                    dialog.dismiss()

            self.page.once("dialog", handle_dialog)
            self.page.locator(locator).click()
        except Exception as e:
            self.log_exception(f"обработке диалога через {locator}", e)
            raise

    def drag_and_drop(self, source_locator: str, target_locator: str):
        self.log(f"Перенос элемента {source_locator} в элемент {target_locator}")
        try:
            self.page.locator(source_locator).drag_to(self.page.locator(target_locator))
        except Exception as e:
            self.log_exception(f"переносе элемента {source_locator} в элемент {target_locator}", e)
            raise

    def click_in_frame(self, frame_selector: str, locator: str):
        self.log(f"Клик по элементу {locator} внутри фрейма {frame_selector}")
        try:
            frame = self.page.frame_locator(frame_selector)
            frame.locator(locator).click()
        except Exception as e:
            self.log_exception(f"клике внутри фрейма {frame_selector}", e)
            raise

    def get_inner_text_in_frame(self, frame_selector: str, locator: str) -> str:
        self.log(f"Получение текста элемента {locator} внутри фрейма {frame_selector}")
        try:
            frame = self.page.frame_locator(frame_selector)
            text = frame.locator(locator).inner_text()
            self.log(f"Текст во фрейме: '{text}'")
            expect(frame.locator(locator))
            return text
        except Exception as e:
            self.log_exception(f"чтении текста во фрейме {frame_selector}", e)
            raise

    def click_button_from_card_in_frame(self, frame_selector: str, card_index: int, locator: str):
        self.log(f"Клик по кнопке {locator} в карточке {card_index} во фрейме {frame_selector}")
        try:
            frame = self.page.frame_locator(frame_selector)
            card = frame.locator('.card').nth(card_index)
            card.locator(locator).click()
        except Exception as e:
            self.log_exception(f"клике по кнопке во фрейме {frame_selector}", e)
            raise

    def get_inner_text_from_card_in_frame(self, frame_selector: str, card_index: int, locator: str) -> str:
        self.log(f"Получение текста из карточки {card_index} во фрейме {frame_selector}")
        try:
            frame = self.page.frame_locator(frame_selector)
            card = frame.locator('.card').nth(card_index)
            text = card.locator(locator).inner_text()
            self.log(f"Текст карточки: '{text}'")
            expect(card.locator(locator))
            return text
        except Exception as e:
            self.log_exception(f"чтении текста карточки во фрейме {frame_selector}", e)
            raise