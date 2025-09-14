import pytest

@pytest.mark.usefixtures('simple_page')
class TestSimplePage:
    def test_simple_page(self, simple_page):
       simple_page.check_simple_button_exists()

    def test_simple_click(self, simple_page):
        simple_page.click_simple_button()
        simple_page.check_result_text_is_('Submitted')