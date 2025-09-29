from pages.base_page import BasePage
from pages.locators.locators import MainPageLocators, SingleCheckboxPageLocators

class SingleCheckboxPage(BasePage):

    def open_home_page(self):
        self.open(MainPageLocators.Base_URL)

    def click_single_checkbox_button_on_home_page(self):
        self.click(MainPageLocators.SELECT_Single_checkbox)

    def click_checkboxes_button(self):
        self.click(SingleCheckboxPageLocators.Checkboxes_BUTTON)

    def select_checkbox_one(self):
        self.select_checkbox(SingleCheckboxPageLocators.One_CHECKBOX)

    def select_checkbox_three(self):
        self.select_checkbox(SingleCheckboxPageLocators.Three_CHECKBOX)

    def verification_one_and_three_checkboxes_selected(self):
        self.is_checkbox_selected(SingleCheckboxPageLocators.One_CHECKBOX,
                                  SingleCheckboxPageLocators.Three_CHECKBOX)

    def click_submit_button(self):
        self.click(SingleCheckboxPageLocators.Submit_BUTTON)

    def verification_one_and_three_checkboxes_result(self):
        self.get_text_content(SingleCheckboxPageLocators.Selected_CHECKBOXES, 'one, three')

    def select_checkbox_two(self):
        self.select_checkbox(SingleCheckboxPageLocators.Two_CHECKBOX)

    def verification_two_checkbox_selected(self):
        self.is_checkbox_selected(SingleCheckboxPageLocators.Two_CHECKBOX)

    def verification_one_and_three_checkboxes_deselected(self):
        self.is_checkbox_deselected(SingleCheckboxPageLocators.One_CHECKBOX,
                                  SingleCheckboxPageLocators.Three_CHECKBOX)

    def verification_two_checkboxes_result(self):
        self.get_text_content(SingleCheckboxPageLocators.Selected_CHECKBOXES, 'two')

    def click_single_checkbox_button(self):
        self.click(SingleCheckboxPageLocators.Single_checkbox_BUTTON)

    def select_single_checkbox(self):
        self.select_checkbox(SingleCheckboxPageLocators.Single_CHECKBOX)

    def deselect_single_checkbox(self):
        self.deselect_checkbox(SingleCheckboxPageLocators.Single_CHECKBOX)

    def verification_single_checkbox_selected(self):
        self.is_checkbox_selected(SingleCheckboxPageLocators.Single_CHECKBOX)

    def verification_single_checkbox_deselected(self):
        self.is_checkbox_deselected(SingleCheckboxPageLocators.Single_CHECKBOX)

    def verification_single_checkboxes_result(self):
        self.get_text_content(SingleCheckboxPageLocators.Selected_CHECKBOXES, 'select me or not')