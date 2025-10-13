from pages.base_page import BasePage
from pages.locators.locators import MainPageLocators, IframesPageLocators

class IframesPage(BasePage):

    def open_home_page(self):
        self.open(MainPageLocators.Base_URL)

    def click_single_ui_elements(self):
        self.click(MainPageLocators.Single_UI_Elements)

    def click_iframes_in_ui_elements(self):
        self.click(MainPageLocators.SELECT_Iframes)

    def click_single_ui_elements_in_frame(self):
        self.click_in_frame(IframesPageLocators.Iframe, MainPageLocators.Single_UI_Elements)

    def click_iframes_in_ui_elements_in_frame(self):
        self.click_in_frame(IframesPageLocators.Iframe, MainPageLocators.SELECT_Iframes)

    def click_navbar_icon(self):
        self.click_in_frame(IframesPageLocators.Iframe, IframesPageLocators.Navbar_ICON)

    def return_to_homepage(self):
        self.click_in_frame(IframesPageLocators.Iframe, IframesPageLocators.Visit_the_homepage_LINK)

    def verification_text_in_footer(self):
        self.get_inner_text_in_frame(IframesPageLocators.Iframe, IframesPageLocators.Footer_TEXT)

    def click_button_view_in_fifth_card(self):
        self.click_button_from_card_in_frame(IframesPageLocators.Iframe,
                                               4, IframesPageLocators.View_BUTTON)

    def click_button_edit_in_sixth_card(self):
        self.click_button_from_card_in_frame(IframesPageLocators.Iframe,
                                               5, IframesPageLocators.Edit_BUTTON)

    def verification_text_in_seventh_card(self):
        self.get_inner_text_from_card_in_frame(IframesPageLocators.Iframe,
                                                 6, IframesPageLocators.Card_Description_TEXT)