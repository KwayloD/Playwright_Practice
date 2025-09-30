from playwright.sync_api import expect

class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def get_inner_text(self, locator: str):
        actual = self.page.locator(locator).inner_text()
        assert actual != "", "Текст по локатору не найден"

    def get_text_content(self, locator: str, expected: str):
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

    def choose_disabled_state(self, locator: str):
        self.page.locator(locator).select_option(value="disabled")

    def element_is_disabled(self, locator: str):
        expect(self.page.locator(locator)).to_be_disabled()

    def choose_enabled_state(self, locator: str):
        self.page.locator(locator).select_option(value="enabled")

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