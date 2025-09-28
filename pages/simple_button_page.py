from pages.base_page import BasePage
from pages.locators.locators import MainPageLocators, SimpleButtonPageLocators

class SimpleButtonPage(BasePage):

    def open_home_page(self):
        self.open(MainPageLocators.Base_URL)

    def click_simple_button_on_home_page(self):
        self.click(MainPageLocators.SELECT_Simple_button)

    def click_simple_button(self):
        self.click(SimpleButtonPageLocators.Simple_BUTTON)

    def click_looks_like_a_button(self):
        self.click(SimpleButtonPageLocators.Looks_like_a_BUTTON)

    def click_disabled_button(self):
        self.click(SimpleButtonPageLocators.Disabled_BUTTON)

    def select_disabled_state(self):
        self.choose_disabled_state(SimpleButtonPageLocators.Select_state_FIELD)

    def verification_disabled_state_of_button(self):
        self.element_is_disabled(SimpleButtonPageLocators.Click_BUTTON)

    def select_enabled_state(self):
        self.choose_enabled_state(SimpleButtonPageLocators.Select_state_FIELD)

    def verification_enabled_state_of_button(self):
        self.element_is_enabled(SimpleButtonPageLocators.Click_BUTTON)

    def click_confirm_button(self):
        self.click(SimpleButtonPageLocators.Click_BUTTON)

    def click_looks_like_a_confirm_button(self):
        self.click(SimpleButtonPageLocators.Click_looks_like_a_BUTTON)

    def verification_input_text_result(self):
        self.get_text_content(SimpleButtonPageLocators.Submitted_TEXT, 'Submitted')