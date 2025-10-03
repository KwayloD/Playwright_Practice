from pages.base_page import BasePage
from pages.locators.locators import MainPageLocators, SelectInputPageLocators

class SelectInputPage(BasePage):

    def open_home_page(self):
        self.open(MainPageLocators.Base_URL)

    def click_select_input_button_on_home_page(self):
        self.click(MainPageLocators.SELECT_Select_input)

    def click_multiple_selects_button(self):
        self.click(SelectInputPageLocators.Multiple_selects_BUTTON)

    def choose_first_language(self):
        self.choose_value_in_select(SelectInputPageLocators.Choose_language_FIELD, '1')

    def choose_fourth_language(self):
        self.choose_value_in_select(SelectInputPageLocators.Choose_language_FIELD, '4')

    def choose_fifth_language(self):
        self.choose_value_in_select(SelectInputPageLocators.Choose_language_FIELD, '5')

    def click_submit_button(self):
        self.click(SelectInputPageLocators.Submit_BUTTON)

    def verification_submitted_language(self):
        self.get_text_content(SelectInputPageLocators.Submitted_TEXT, 'Python')

    def choose_first_place(self):
        self.choose_value_in_select(SelectInputPageLocators.Choose_the_place_you_want_to_go_FIELD,
                                    SelectInputPageLocators.First_place_VALUE[0])

    def choose_first_transport(self):
        self.choose_value_in_select(SelectInputPageLocators.Choose_how_you_want_to_get_there_FIELD,
                                    SelectInputPageLocators.First_transport_VALUE[0])

    def choose_first_time(self):
        self.choose_value_in_select(SelectInputPageLocators.Choose_when_you_want_to_go_FIELD,
                                    SelectInputPageLocators.First_time_VALUE[0])

    def choose_second_place(self):
        self.choose_value_in_select(SelectInputPageLocators.Choose_the_place_you_want_to_go_FIELD,
                                    SelectInputPageLocators.Second_place_VALUE[0])

    def choose_second_transport(self):
        self.choose_value_in_select(SelectInputPageLocators.Choose_how_you_want_to_get_there_FIELD,
                                    SelectInputPageLocators.Second_transport_VALUE[0])

    def choose_second_time(self):
        self.choose_value_in_select(SelectInputPageLocators.Choose_when_you_want_to_go_FIELD,
                                    SelectInputPageLocators.Second_time_VALUE[0])

    def verification_the_first_choice_of_the_result(self):
        self.get_text_content(SelectInputPageLocators.Submitted_TEXT,
                              f'to go by {SelectInputPageLocators.First_transport_VALUE[1].lower()} '
                              f'to the {SelectInputPageLocators.First_place_VALUE[1].lower()} '
                              f'{SelectInputPageLocators.First_time_VALUE[1].lower()}')

    def verification_the_second_choice_of_the_result(self):
        self.get_text_content(SelectInputPageLocators.Submitted_TEXT,
                              f'to go by {SelectInputPageLocators.Second_transport_VALUE[1].lower()} '
                              f'to the {SelectInputPageLocators.Second_place_VALUE[1].lower()} '
                              f'{SelectInputPageLocators.Second_time_VALUE[1].lower()}')