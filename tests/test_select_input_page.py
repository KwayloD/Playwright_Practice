from pages.select_input_page import SelectInputPage

def test_select_input_page(page):
    base = SelectInputPage(page)

    base.open_home_page()
    base.click_select_input_button_on_home_page()
    base.choose_fifth_language()
    base.choose_fourth_language()
    base.choose_first_language()
    base.click_submit_button()
    base.verification_submitted_language()

    base.click_multiple_selects_button()
    base.choose_first_place()
    base.choose_first_transport()
    base.choose_first_time()
    base.click_submit_button()
    base.verification_the_first_choice_of_the_result()

    base.choose_second_place()
    base.choose_second_transport()
    base.choose_second_time()
    base.click_submit_button()
    base.verification_the_second_choice_of_the_result()