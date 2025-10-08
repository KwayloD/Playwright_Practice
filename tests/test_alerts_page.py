from pages.alerts_page import AlertsPage

def test_new_tab_page(page):
    base = AlertsPage(page)

    base.open_home_page()
    base.click_single_ui_elements()
    base.click_alerts_in_ui_elements()

    base.click_prompt_box()
    base.click_a_button_with_prompt_box_and_entered_prompt()
    base.verification_prompt_ok_result()

    base.click_a_button_with_prompt_box_and_canceled_prompt()
    base.verification_prompt_cancel_result()

    base.click_confirmation_box()
    base.click_a_button_with_confirmation_box_and_ok_choice()
    base.verification_confirmation_ok_result()

    base.click_a_button_with_confirmation_box_and_cancel_choice()
    base.verification_confirmation_cancel_result()

    base.click_alert_box()
    base.click_a_button_with_alert_box()