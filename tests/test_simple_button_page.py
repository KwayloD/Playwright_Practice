from pages.simple_button_page import SimpleButtonPage

def test_simple_button_page(page):
    base = SimpleButtonPage(page)

    base.open_home_page()
    base.click_simple_button_on_home_page()

    base.click_disabled_button()
    base.select_enabled_state()
    base.verification_enabled_state_of_button()
    base.select_disabled_state()
    base.verification_disabled_state_of_button()
    base.select_enabled_state()
    base.verification_enabled_state_of_button()
    base.click_confirm_button()
    base.verification_input_text_result()

    base.click_looks_like_a_button()
    base.click_looks_like_a_confirm_button()
    base.verification_input_text_result()

    base.click_simple_button()
    base.click_confirm_button()
    base.verification_input_text_result()