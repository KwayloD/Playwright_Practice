from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators.simple_page_locators import SimplePageLocators as Loc

class SimplePage(BasePage):
    url = 'https://www.qa-practice.com/elements/button/simple'

    def check_simple_button_exists(self):
        expect(self.page.locator(Loc.SIMPLE_BUTTON)).to_be_visible()

    def click_simple_button(self):
        self.page.locator(Loc.SIMPLE_BUTTON).click()

    def check_result_text_is_(self, text):
        expect(self.page.locator(Loc.RESULT_TEXT)).to_have_text(text)