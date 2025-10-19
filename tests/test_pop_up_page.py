from pages.pop_up_page import PopUpPage

def test_pop_up_page(page):
    base = PopUpPage(page)

    base.open_home_page()
    base.click_single_ui_elements()
    base.click_pop_up_in_ui_elements()
    base.click_launch_pop_up()
    base.verification_of_title_pop_up()
    base.click_close_button()

    base.click_launch_pop_up()
    base.verification_of_title_pop_up()
    base.check_checkbox()
    base.verification_checkbox_is_selected()
    base.click_send_button()
    base.verification_the_submitted_result()

    base.click_launch_pop_up()
    base.verification_of_title_pop_up()
    base.verification_checkbox_is_deselected()
    base.click_send_button()
    base.verification_the_unsent_result()

    base.click_iframe_pop_up()
    base.click_launch_pop_up()
    base.click_close_button()

    base.click_launch_pop_up()
    base.click_check_button()
    base.fill_incorrect_text_in_field()
    base.click_submit()
    base.verification_incorrect_result()

    base.click_launch_pop_up()
    base.click_check_button()
    base.fill_correct_text_in_field()
    base.click_submit()
    base.verification_correct_result()

