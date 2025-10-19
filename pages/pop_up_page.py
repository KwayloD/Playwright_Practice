from pages.base_page import BasePage
from pages.locators.locators import MainPageLocators, PopUpPageLocators

class PopUpPage(BasePage):

    def open_home_page(self):
        self.open(MainPageLocators.Base_URL)

    def click_single_ui_elements(self):
        self.click(MainPageLocators.Single_UI_Elements)

    def click_pop_up_in_ui_elements(self):
        self.click(MainPageLocators.SELECT_PopUp)

    def click_launch_pop_up(self):
        self.click(PopUpPageLocators.Launch_PopUp_BUTTON)

    def verification_of_title_pop_up(self):
        self.get_inner_text(PopUpPageLocators.Title_PopUp)

    def check_checkbox(self):
        self.select_checkbox(PopUpPageLocators.Checkbox)

    def verification_checkbox_is_selected(self):
        self.is_checkbox_selected(PopUpPageLocators.Checkbox)

    def verification_checkbox_is_deselected(self):
        self.is_checkbox_deselected(PopUpPageLocators.Checkbox)

    def click_send_button(self):
        self.click_by_text(PopUpPageLocators.Send_BUTTON)

    def click_close_button(self):
        self.click_by_text(PopUpPageLocators.Close_BUTTON)

    def click_check_button(self):
        self.click_by_text(PopUpPageLocators.Check_BUTTON)

    def verification_the_submitted_result(self):
        self.get_text_content(PopUpPageLocators.Result, 'select me or not')

    def verification_the_unsent_result(self):
        self.get_text_content(PopUpPageLocators.Result, 'None')

    def click_iframe_pop_up(self):
        self.click(PopUpPageLocators.Iframe_PopUp_BUTTON)

    def fill_correct_text_in_field(self):
        self.fill(PopUpPageLocators.Text_FIELD, 'I am the text you want to copy')

    def fill_incorrect_text_in_field(self):
        self.fill(PopUpPageLocators.Text_FIELD, 'I am the text you not want to copy')

    def click_submit(self):
        self.click(PopUpPageLocators.Submit_BUTTON)

    def verification_correct_result(self):
        self.get_text_content(PopUpPageLocators.Iframe_RESULT, 'Correct!')

    def verification_incorrect_result(self):
        self.get_text_content(PopUpPageLocators.Iframe_RESULT, 'Nope. Better luck next time!')