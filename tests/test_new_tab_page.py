from pages.new_tab_page import NewTabPage

class TestNewTabPage:

    def test_new_tabs(self, page):
        base = NewTabPage(page)
        base.open_home_page()
        base.click_single_ui_elements()
        base.click_new_tab_in_ui_elements()
        base.click_new_tab_button()
        base.click_button_to_open_new_page()
        base.switch_to_new_tab_after_click_button()
        base.verification_new_page_result()
        base.click_new_tab_link()
        base.click_link_to_open_new_page()
        base.switch_to_new_tab_after_click_link()
        base.verification_new_page_result()
        base.switch_to_first_tab()
        base.return_to_the_homepage()
        base.verification_description_text()
        base.close_third_tab()
        base.close_second_tab()
        base.close_first_tab()