from pages.base_page import BasePage
from pages.locators.locators import MainPageLocators, TextInputPageLocators

class TextInputPage(BasePage):

    def open_home_page(self):
        self.open(MainPageLocators.BASE_URL)

    def back_to_the_home(self):
        self.go_back()

    def click_text_input(self):
        self.click(MainPageLocators.SELECT_Text_input)

    def click_button_text_input(self):
        self.click(TextInputPageLocators.Text_input_BUTTON)

    def click_button_email_field(self):
        self.click(TextInputPageLocators.Email_field_BUTTON)

    def click_button_password_field(self):
        self.click(TextInputPageLocators.Password_field_BUTTON)

    def submit_field_text_input(self):
        self.fill_and_press_enter(TextInputPageLocators.Text_FIELD, 'playwright')

    def submit_field_email_field(self):
        self.fill_and_press_enter(TextInputPageLocators.Email_FIELD, 'playwright@gmail.com')

    def submit_field_password_field(self):
        self.fill_and_press_enter(TextInputPageLocators.Password_FIELD, 'p1@yWr19h!')

    def verification_input_text_result(self):
        self.get_text_content(TextInputPageLocators.INPUT_RESULT, 'playwright')

    def verification_input_email_result(self):
        self.get_text_content(TextInputPageLocators.INPUT_RESULT, 'playwright@gmail.com')

    def verification_input_password_result(self):
        self.get_text_content(TextInputPageLocators.INPUT_RESULT, 'p1@yWr19h!')