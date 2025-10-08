from pages.base_page import BasePage
from pages.locators.locators import MainPageLocators, AlertsPageLocators

class AlertsPage(BasePage):

    def open_home_page(self):
        self.open(MainPageLocators.Base_URL)

    def click_single_ui_elements(self):
        self.click(MainPageLocators.Single_UI_Elements)

    def click_alerts_in_ui_elements(self):
        self.click(MainPageLocators.SELECT_Alerts)

    def click_alert_box(self):
        self.click(AlertsPageLocators.Alert_BUTTON)

    def click_confirmation_box(self):
        self.click(AlertsPageLocators.Confirmation_BUTTON)

    def click_prompt_box(self):
        self.click(AlertsPageLocators.Prompt_BUTTON)

    def click_a_button_with_alert_box(self):
        self.dialog_alert(AlertsPageLocators.Click_BUTTON)

    def click_a_button_with_confirmation_box_and_ok_choice(self):
        self.dialog_alert(AlertsPageLocators.Click_BUTTON, True)

    def click_a_button_with_confirmation_box_and_cancel_choice(self):
        self.dialog_alert(AlertsPageLocators.Click_BUTTON, False)

    def click_a_button_with_prompt_box_and_entered_prompt(self):
        self.dialog_alert(AlertsPageLocators.Click_BUTTON, True, 'The prompt is entered')

    def click_a_button_with_prompt_box_and_canceled_prompt(self):
        self.dialog_alert(AlertsPageLocators.Click_BUTTON, False, 'The prompt is entered')

    def verification_confirmation_ok_result(self):
        self.get_text_content(AlertsPageLocators.RESULT, 'Ok')

    def verification_confirmation_cancel_result(self):
        self.get_text_content(AlertsPageLocators.RESULT, 'Cancel')

    def verification_prompt_ok_result(self):
        self.get_text_content(AlertsPageLocators.RESULT, 'The prompt is entered')

    def verification_prompt_cancel_result(self):
        self.get_text_content(AlertsPageLocators.RESULT, 'You canceled the prompt')