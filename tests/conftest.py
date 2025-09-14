import pytest
from pages.simple_page import SimplePage

@pytest.fixture
def simple_page(page):
    simple_page = SimplePage(page)
    simple_page.open()
    return simple_page