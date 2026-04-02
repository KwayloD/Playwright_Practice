from pages.alerts_page import AlertsPage

class TestAlertsPage:
    def test_prompt_box_with_entered_prompt(self, page):
        base = AlertsPage(page)
        base.open_home_page()
        base.click_single_ui_elements()
        base.click_alerts_in_ui_elements()
        base.click_prompt_box()
        base.click_a_button_with_prompt_box_and_entered_prompt()
        base.verification_prompt_ok_result()

    def test_prompt_box_with_canceled_prompt(self, page):
        base = AlertsPage(page)
        base.open_alerts_page()
        base.click_prompt_box()
        base.click_a_button_with_prompt_box_and_canceled_prompt()
        base.verification_prompt_cancel_result()

    def test_confirmation_box_ok_result(self, page):
        base = AlertsPage(page)
        base.open_alerts_page()
        base.click_confirmation_box()
        base.click_a_button_with_confirmation_box_and_ok_choice()
        base.verification_confirmation_ok_result()

    def test_confirmation_box_cancel_result(self, page):
        base = AlertsPage(page)
        base.open_alerts_page()
        base.click_confirmation_box()
        base.click_a_button_with_confirmation_box_and_cancel_choice()
        base.verification_confirmation_cancel_result()

    def test_alert_box(self, page):
        base = AlertsPage(page)
        base.open_alerts_page()
        base.click_alert_box()
        base.click_a_button_with_alert_box()