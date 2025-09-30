from pages.base_page import BasePage
from pages.locators.locators import MainPageLocators, TextAreaPageLocators

class TextAreaPage(BasePage):

    def open_home_page(self):
        self.open(MainPageLocators.Base_URL)

    def click_text_area_button_on_home_page(self):
        self.click(MainPageLocators.SELECT_Text_area)

    def click_textarea_button(self):
        self.click(TextAreaPageLocators.Textarea_BUTTON)

    def click_multiple_textareas_button(self):
        self.click(TextAreaPageLocators.Multiple_textareas_BUTTON)

    def fill_text_area_field(self):
        self.fill(TextAreaPageLocators.Text_area_FIELD, 'Текст на проверку')

    def fill_first_chapter_field(self):
        self.fill(TextAreaPageLocators.First_chapter_FIELD, 'Текст')

    def fill_second_chapter_field(self):
        self.fill(TextAreaPageLocators.Second_chapter_FIELD, 'на')

    def fill_third_chapter_field(self):
        self.fill(TextAreaPageLocators.Third_chapter_FIELD, 'проверку')

    def click_submit_button(self):
        self.click(TextAreaPageLocators.Submit_BUTTON)

    def verification_input_text_area_result(self):
        self.get_text_content(TextAreaPageLocators.Entered_TEXT, 'Текст на проверку')

    def verification_input_text_chapters_result(self):
        self.get_text_content(TextAreaPageLocators.Entered_TEXT, 'ТекстНаПроверку')