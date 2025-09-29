from pages.single_checkbox_page import SingleCheckboxPage

def test_single_checkbox_page(page):
    base = SingleCheckboxPage(page)

    base.open_home_page()
    base.click_single_checkbox_button_on_home_page()

    base.click_checkboxes_button()
    base.select_checkbox_one()
    base.select_checkbox_three()
    base.verification_one_and_three_checkboxes_selected()
    base.click_submit_button()
    base.verification_one_and_three_checkboxes_result()
    base.select_checkbox_two()
    base.verification_two_checkbox_selected()
    base.verification_one_and_three_checkboxes_deselected()
    base.click_submit_button()
    base.verification_two_checkboxes_result()

    base.click_single_checkbox_button()
    base.select_single_checkbox()
    base.verification_single_checkbox_selected()
    base.deselect_single_checkbox()
    base.verification_single_checkbox_deselected()
    base.select_single_checkbox()
    base.verification_single_checkbox_selected()
    base.click_submit_button()
    base.verification_single_checkboxes_result()