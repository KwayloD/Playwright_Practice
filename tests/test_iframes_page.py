from pages.iframes_page import IframesPage

class TestIframesPage:
    def test_navbar(self, page):
        base = IframesPage(page)

        base.open_home_page()
        base.click_single_ui_elements()
        base.click_iframes_in_ui_elements()
        base.click_navbar_icon()
        base.click_navbar_icon()

    def test_cards(self, page):
        base = IframesPage(page)
        base.open_iframes_page()
        base.click_button_view_in_fifth_card()
        base.click_button_edit_in_sixth_card()
        base.verification_text_in_seventh_card()

    def test_footer(self, page):
        base = IframesPage(page)
        base.open_iframes_page()
        base.verification_text_in_footer()
        base.return_to_homepage()
        base.click_single_ui_elements_in_frame()
        base.click_iframes_in_ui_elements_in_frame()