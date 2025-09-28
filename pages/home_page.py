from pages.base_page import BasePage
from pages.locators.locators import MainPageLocators

class HomePage(BasePage):

    def open_home_page(self):
        self.open(MainPageLocators.Base_URL)

    def back_to_the_home(self):
        self.go_back()

    def get_description_text(self):
        self.get_inner_text(MainPageLocators.Description_TEXT)

    def click_text_input(self):
        self.click(MainPageLocators.SELECT_Text_input)

    def verification_title_text_input(self):
        self.get_text_content(MainPageLocators.Title_TEXT, expected=' Input field ')

    def click_simple_button(self):
        self.click(MainPageLocators.SELECT_Simple_button)

    def verification_title_simple_button(self):
        self.get_text_content(MainPageLocators.Title_TEXT, expected='Buttons')

    def click_single_checkbox(self):
        self.click(MainPageLocators.SELECT_Single_checkbox)

    def verification_title_single_checkbox(self):
        self.get_text_content(MainPageLocators.Title_TEXT, expected='Checkboxes')

    def click_text_area(self):
        self.click(MainPageLocators.SELECT_Text_area)

    def verification_title_text_area(self):
        self.get_text_content(MainPageLocators.Title_TEXT, expected='TextArea inputs')

    def click_select_input(self):
        self.click(MainPageLocators.SELECT_Select_input)

    def verification_title_select_input(self):
        self.get_text_content(MainPageLocators.Title_TEXT, expected='Select inputs')