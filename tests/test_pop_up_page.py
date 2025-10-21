from pages.pop_up_page import PopUpPage

class TestPopUpPage:
    def test_close_button_on_modal(self, page):
        base = PopUpPage(page)
        base.open_home_page()
        base.click_single_ui_elements()
        base.click_pop_up_in_ui_elements()
        base.click_launch_pop_up()
        base.verification_of_title_pop_up()
        base.click_close_button()

    def test_send_button_on_modal_with_submitted_result(self, page):
        base = PopUpPage(page)
        base.open_pop_up_page()
        base.click_modal_button()
        base.click_launch_pop_up()
        base.verification_of_title_pop_up()
        base.check_checkbox()
        base.verification_checkbox_is_selected()
        base.click_send_button()
        base.verification_the_submitted_result()

    def test_send_button_on_modal_with_unsent_result(self, page):
        base = PopUpPage(page)
        base.open_pop_up_page()
        base.click_modal_button()
        base.click_launch_pop_up()
        base.verification_of_title_pop_up()
        base.verification_checkbox_is_deselected()
        base.click_send_button()
        base.verification_the_unsent_result()

    def test_close_button_on_iframe_pop_up(self, page):
        base = PopUpPage(page)
        base.open_pop_up_page()
        base.click_iframe_pop_up()
        base.click_launch_pop_up()
        base.click_close_button()

    def test_incorrect_result_on_iframe_pop_up(self, page):
        base = PopUpPage(page)
        base.open_pop_up_page()
        base.click_iframe_pop_up()
        base.click_launch_pop_up()
        base.click_check_button()
        base.fill_incorrect_text_in_field()
        base.click_submit()
        base.verification_incorrect_result()

    def test_correct_result_on_iframe_pop_up(self, page):
        base = PopUpPage(page)
        base.open_pop_up_page()
        base.click_iframe_pop_up()
        base.click_launch_pop_up()
        base.click_check_button()
        base.fill_correct_text_in_field()
        base.click_submit()
        base.verification_correct_result()

