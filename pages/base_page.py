from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def get_inner_text(self, locator: str):
        self.page.wait_for_selector(locator)
        actual = self.page.locator(locator).inner_text()
        assert actual != "", "Текст по локатору не найден"

    def get_text_content(self, locator: str, expected: str):
        self.page.wait_for_selector(locator)
        actual = self.page.locator(locator).text_content()
        assert actual == expected, f"Ожидали '{expected}', а получили '{actual}'"

    def click(self, locator: str):
        self.page.locator(locator).click()

    def go_back(self,):
        self.page.go_back()

    def fill(self, locator: str, text: str):
        self.page.locator(locator).fill(text)

    def fill_and_press_enter(self, locator: str, text: str):
        self.page.locator(locator).fill(text)
        self.page.locator(locator).press("Enter")

    def choose_value_in_select(self, locator: str, value: str):
        self.page.locator(locator).select_option(value=value)

    def element_is_disabled(self, locator: str):
        expect(self.page.locator(locator)).to_be_disabled()

    def element_is_enabled(self, locator: str):
        expect(self.page.locator(locator)).to_be_enabled()

    def select_checkbox(self, locator: str):
        self.page.locator(locator).check()

    def deselect_checkbox(self, locator: str):
        self.page.locator(locator).uncheck()

    def is_checkbox_selected(self, *locators: str):
        for locator in locators:
            expect(self.page.locator(locator)).to_be_checked()

    def is_checkbox_deselected(self, *locators: str):
        for locator in locators:
            expect(self.page.locator(locator)).not_to_be_checked()

    def open_new_tab(self, locator: str) -> Page:
        with self.page.context.expect_page() as new_page_info:
            self.page.locator(locator).click()
        new_tab = new_page_info.value
        new_tab.wait_for_load_state()
        new_tab.bring_to_front()
        return new_tab

    def switch_to_tab(self, index: int) -> Page:
        new_tab = self.page.context.pages[index]
        new_tab.bring_to_front()
        self.page = new_tab
        return new_tab

    def close_tab_by_index(self, index: int):
        if index < len(self.page.context.pages):
            self.page.context.pages[index].close()

    def dialog_alert(self, locator: str, accept: bool = True, prompt_text: str = None):
        def handle_dialog(dialog):
            if dialog.type == "prompt" and prompt_text:
                dialog.accept(prompt_text) if accept else dialog.dismiss()
            elif accept:
                dialog.accept()
            else:
                dialog.dismiss()

        self.page.once("dialog", handle_dialog)
        self.page.locator(locator).click()