from pages.text_area_page import TextAreaPage

class TestTextAreaPage:
    def test_textarea_button(self, page):
        base = TextAreaPage(page)
        base.open_home_page()
        base.click_text_area_button_on_home_page()
        base.fill_text_area_field()
        base.click_submit_button()
        base.verification_input_text_area_result()

    def test_multiple_textareas_button(self, page):
        base = TextAreaPage(page)
        base.open_text_area_page()
        base.click_multiple_textareas_button()
        base.fill_first_chapter_field()
        base.fill_second_chapter_field()
        base.fill_third_chapter_field()
        base.click_submit_button()
        base.verification_input_text_chapters_result()