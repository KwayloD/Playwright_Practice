from pages.text_input_page import TextInputPage

def test_text_input_page(page):
    base = TextInputPage(page)

    base.open_home_page()
    base.click_text_input()

    base.click_button_text_input()
    base.submit_field_text_input()
    base.verification_input_text_result()

    base.click_button_email_field()
    base.submit_field_email_field()
    base.verification_input_email_result()

    base.click_button_password_field()
    base.submit_field_password_field()
    base.verification_input_password_result()