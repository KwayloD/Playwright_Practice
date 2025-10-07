from pages.base_page import BasePage
from pages.locators.locators import MainPageLocators, NewTabPageLocators

class NewTabPage(BasePage):

    def open_home_page(self):
        self.open(MainPageLocators.Base_URL)

    def click_single_ui_elements(self):
        self.click(MainPageLocators.Single_UI_Elements)

    def click_new_tab_in_ui_elements(self):
        self.click(MainPageLocators.SELECT_New_tab)

    def click_new_tab_link(self):
        self.click(NewTabPageLocators.New_tab_link_BUTTON)

    def click_new_tab_button(self):
        self.click(NewTabPageLocators.New_tab_button_BUTTON)

    def click_link_to_open_new_page(self):
        self.open_new_tab(NewTabPageLocators.To_open_a_new_tab_LINK)

    def click_button_to_open_new_page(self):
        self.open_new_tab(NewTabPageLocators.To_open_a_new_tab_BUTTON)

    def switch_to_new_tab_after_click_button(self):
        self.switch_to_tab(1)

    def switch_to_new_tab_after_click_link(self):
        self.switch_to_tab(2)

    def switch_to_first_tab(self):
        self.switch_to_tab(0)

    def verification_single_checkboxes_result(self):
        self.get_text_content(NewTabPageLocators.New_tab_MESSAGE, 'I am a new page in a new tab')

    def return_to_the_homepage(self):
        self.page.locator('#sidebar span').filter(has_text=MainPageLocators.Homepage).click()

    def verification_description_text(self):
        self.get_inner_text(MainPageLocators.Description_TEXT)

    def close_third_tab(self):
        self.close_tab_by_index(2)

    def close_second_tab(self):
        self.close_tab_by_index(1)

    def close_first_tab(self):
        self.close_tab_by_index(0)