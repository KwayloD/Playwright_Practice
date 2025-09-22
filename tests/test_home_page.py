from pages.home_page import HomePage

def test_home_page_buttons(page):
    base = HomePage(page)

    base.open_home_page()
    base.get_description_text()
    base.click_text_input()
    base.verification_title_text_input()
    base.go_back()
    base.click_simple_button()
    base.verification_title_simple_button()
    base.go_back()
    base.click_single_checkbox()
    base.verification_title_single_checkbox()
    base.go_back()
    base.click_text_area()
    base.verification_title_text_area()
    base.go_back()
    base.click_select_input()
    base.verification_title_select_input()
    base.go_back()